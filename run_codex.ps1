param(
    [Parameter(Mandatory = $true, Position = 0)]
    [string]$Prompt,
    [int]$MaxSteps = 25,
    [switch]$Safe
)

$repo = Split-Path -Parent $MyInvocation.MyCommand.Path
$env:CODEX_HOME = Join-Path $repo ".codex"

$argsList = @(
    "-Prompt", $Prompt,
    "-MaxSteps", "$MaxSteps"
)

if (-not $Safe) {
    $argsList += "-Unsafe"
}

& (Join-Path $repo "run_autoflow.ps1") @argsList
