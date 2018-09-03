import hudson.Functions;
import hudson.model.*;
import hudson.tasks.*;
import org.jenkinsci.plugins.workflow.cps.*;
import org.jenkinsci.plugins.workflow.job.*;
import org.junit.*;
import org.jvnet.hudson.test.*;

public class BasicExampleTest {
  @Rule public JenkinsRule j = new JenkinsRule(); 
  @ClassRule public static BuildWatcher bw = new BuildWatcher(); 

  @Test public void freestyleEcho() throws Exception {
    final String command = "echo hello";

    // Create a new freestyle project with a unique name, with an "Execute shell" build step;
    // if running on Windows, this will be an "Execute Windows batch command" build step
    FreeStyleProject project = j.createFreeStyleProject();
    Builder step = Functions.isWindows() ? new BatchFile(command) : new Shell(command); 
    project.getBuildersList().add(step);

    // Enqueue a build of the project, wait for it to complete, and assert success
    FreeStyleBuild build = j.buildAndAssertSuccess(project);

    // Assert that the console log contains the output we expect
    j.assertLogContains(command, build);
  }

  @Test public void pipelineEcho() throws Exception {
    // Create a new Pipeline with the given (Scripted Pipeline) definition
    WorkflowJob project = j.createProject(WorkflowJob.class); 
    project.setDefinition(new CpsFlowDefinition("node { echo 'hello' }", true)); 

    // Enqueue a build of the Pipeline, wait for it to complete, and assert success
    WorkflowRun build = j.buildAndAssertSuccess(project);

    // Assert that the console log contains the output we expect
    j.assertLogContains("hello", build);
  }
}