# Jenkins Practice

A tiny, dependency-free Python app to experiment with Jenkins pipelines safely.

## What the Jenkinsfile does
1. **Checkout** - pulls this repo
2. **Build** - prints the Python version on the agent
3. **Test** - runs `python3 -m unittest` (2 tests in `test_app.py`)
4. **Package** - creates and archives `app.tar.gz`
5. **Deploy** - simulated deploy (echo/run only, nothing real is changed)

`post` block prints whether the build succeeded or failed.

## Run locally first (optional)
```bash
python3 app.py
python3 -m unittest discover -s . -p "test_*.py" -v
```

## Use it in Jenkins
1. Create a **Pipeline** job in Jenkins
2. Under *Pipeline > Definition*, choose **Pipeline script from SCM**
3. SCM = Git, paste this repo's GitHub URL, branch `*/main`
4. Script Path = `Jenkinsfile` -> Save -> **Build Now**

Try changing a test on purpose (make it fail) and watch the pipeline go red,
then fix it and watch it go green. That's the best way to learn Jenkins.
