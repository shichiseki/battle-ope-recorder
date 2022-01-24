const childProcess = require("child_process")

const proc = childProcess.spawn(
    // "pyinstaller",
    "cxfreeze",
    [
        "--target-dir ./build/python-dist",
        "backend/app.py",
    ],
    {
        shell: true,
    }
);

proc.stdout.on("data", (data) => {
    process.stdout.write(data.toString());
});

proc.stderr.on("data", (data) => {
    process.stdout.write(data.toString());
});

proc.on("exit", (code) => {
    process.stdout.write("cxfreeze exited with code " + code.toString());
});