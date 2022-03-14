import nox


locations = "reimbursement_manager", "tests", "noxfile.py"


@nox.session()
def tests(session):
    args = session.posargs or ["--cov"]
    session.run("poetry", "install", external=True)
    session.run("pytest", *args)


@nox.session()
def flake8(session):
    args = session.posargs or locations
    session.install("flake8", "flake8-import-order")
    session.run("flake8", *args)
