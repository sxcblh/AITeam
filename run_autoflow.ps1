param(
    [Parameter(Mandatory = $true)]
    [string]$Prompt,
    [int]$MaxSteps = 25,
    [switch]$Unsafe
)

$repo = Split-Path -Parent $MyInvocation.MyCommand.Path
$env:CODEX_HOME = Join-Path $repo ".codex"

$argsList = @(
    "--prompt", $Prompt,
    "--max-steps", "$MaxSteps",
    "--repo", $repo
)

if ($Unsafe) {
    $argsList += "--unsafe"
}

python (Join-Path $repo "tools/auto_flow.py") @argsList
