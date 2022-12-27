# UpgradeAdvisor
A simple, easy-to-use PC upgrade advisor made using Python referencing the [UserBenchmark](https://www.userbenchmark.com) API.

## How-to
* Download the benchmarking tool from UserBenchmark [here](https://www.userbenchmark.com/resources/download/UserBenchmarkInstaller.exe).
* Export the benchmark results to a text-file. To do this, simple copy-paste the results into a text file.
* Run the Python script or the Windows executable.

## Usage
If you're using the Windows binary:
`upgrade_advisor <text file> <percentage improvement>`

If you're using the Python script instead, similarly:
`python upgrade_advisor.py <text file> <percentage improvement>`

For example, if the results are stored in `results.txt` and you want a `30`% improvement, the command would be:

`upgrade_advisor results.txt 30`

The output would be a list of potentially upgradable components which you can then check out.
