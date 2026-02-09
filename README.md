<<<<<<< HEAD
Employee Leave Request App

1. Setup
- bench get-app <repo-url>
- bench install-app employee_leave_app
- bench migrate

2. Features
- Auto total days calculation
- Date validation
- HR-only approval
- No self approval

3. Logic Flow
Employee → Create Request → HR Review → Approve/Reject
=======
### Employee Leave App

employee leave management

### Installation

You can install this app using the [bench](https://github.com/frappe/bench) CLI:

```bash
cd $PATH_TO_YOUR_BENCH
bench get-app $URL_OF_THIS_REPO --branch develop
bench install-app employee
```

### Contributing

This app uses `pre-commit` for code formatting and linting. Please [install pre-commit](https://pre-commit.com/#installation) and enable it for this repository:

```bash
cd apps/employee
pre-commit install
```

Pre-commit is configured to use the following tools for checking and formatting your code:

- ruff
- eslint
- prettier
- pyupgrade

### CI

This app can use GitHub Actions for CI. The following workflows are configured:

- CI: Installs this app and runs unit tests on every push to `develop` branch.
- Linters: Runs [Frappe Semgrep Rules](https://github.com/frappe/semgrep-rules) and [pip-audit](https://pypi.org/project/pip-audit/) on every pull request.


### License

mit
>>>>>>> 0a87a1a (feat: Initialize App)
