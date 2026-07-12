from app.workflows.resume_workflow import ResumeWorkflow

workflow = ResumeWorkflow()

resume = workflow.execute(
    "data/resumes/9d16b0c6fcb946c7a6e902cbc184ac2d.pdf"
)

print("=" * 80)
print(resume)
print("=" * 80)
