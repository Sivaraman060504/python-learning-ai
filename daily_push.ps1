Set-Location "D:\python_learning"

git add .

$changes = git status --porcelain

if ($changes) {

    $today = Get-Date -Format "yyyy-MM-dd"

    git commit -m "Python practice - $today"

    git push origin main

    Write-Host "GitHub updated successfully! 🚀"

} else {

    Write-Host "No new changes to commit."

}