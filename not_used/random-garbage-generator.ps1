function Application_Main {
    for ($i = 0; $i -lt 24; $i++) {
        $rand = Get-Random-String -Count 48
        if ($i -ne 0) {
            Write-Output $rand | Out-File -FilePath "random-garbage" -Append -Encoding "UTF8"
        } else {
            Write-Output $rand | Out-File -FilePath "random-garbage" -Encoding "UTF8"
        } Write-Output $rand
    }
    Write-Output ""
    Start-Process -FilePath "git.exe" -ArgumentList "add", "--all"  -Wait -NoNewWindow -PassThru
    Start-Process -FilePath "git.exe" -ArgumentList "commit", "-m", "`"asd`""  -Wait -NoNewWindow -PassThru
    Start-Process -FilePath "git.exe" -ArgumentList "push"  -Wait -NoNewWindow -PassThru
    Write-Output ""
    Write-Output "Done."
}

# random string a-z A-Z 0-9
function Get-Random-String {
    param (
        [int]$Count
    )

    return -join ((65..90) + (97..122) + (48..57) | Get-Random -Count $Count | ForEach-Object {[char]$_})
}

Application_Main