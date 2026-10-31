# PowerShell equivalent of download-official-sources.sh. Run from anywhere; it changes to the repo root itself.
Set-Location (Join-Path $PSScriptRoot "..")  # repo root
$lines = Get-Content (Join-Path $PSScriptRoot "download-official-sources.sh") | Where-Object { $_ -match '^dl ' }
foreach ($l in $lines) {
  if ($l -match '^dl (\S+) "([^"]+)"') {
    $out = $matches[1] -replace '\$\(date \+%Y-%m-%d\)', (Get-Date -Format 'yyyy-MM-dd')
    $url = $matches[2]
    try { Invoke-WebRequest -Uri $url -OutFile $out -UseBasicParsing; Write-Host "OK   $out" }
    catch { Write-Host "FAIL $out <- $url" }
  }
}
Get-ChildItem 01-Original-Legislation,02-Amendments,03-Gazettes-and-Commencement,04-Regulations-and-Rules,05-DPA-Guidelines-and-Circulars -Filter *.pdf -Recurse |
  ForEach-Object { "{0}  {1}" -f (Get-FileHash $_.FullName -Algorithm SHA256).Hash.ToLower(), $_.FullName.Substring((Get-Location).Path.Length+1).Replace('\','/') } |
  Set-Content 14-Project-Documentation/CHECKSUMS.txt
Add-Content 14-Project-Documentation/CHECKSUMS.txt ("Done. Retrieved on " + (Get-Date).ToUniversalTime().ToString('yyyy-MM-ddTHH:mmZ'))
