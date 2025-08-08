[Setup]
AppName=Caselist Maker
AppVersion=1.0.0
AppPublisher=Tanmay Garg
AppPublisherURL=https://github.com/CODERTG2/CaselistMaker
DefaultDirName={autopf}\CaselistMaker
DefaultGroupName=Caselist Maker
OutputDir=installers
OutputBaseFilename=CaselistMaker-Setup-v1.0.0
Compression=lzma
SolidCompression=yes
WizardStyle=modern
UninstallDisplayIcon={app}\CaselistMaker.exe

[Languages]
Name: "english"; MessagesFile: "compiler:Default.isl"

[Tasks]
Name: "desktopicon"; Description: "{cm:CreateDesktopIcon}"; GroupDescription: "{cm:AdditionalIcons}"; Flags: unchecked

[Files]
Source: "dist\main\*"; DestDir: "{app}"; Flags: ignoreversion recursesubdirs createallsubdirs

[Icons]
Name: "{group}\Caselist Maker"; Filename: "{app}\CaselistMaker.exe"
Name: "{autodesktop}\Caselist Maker"; Filename: "{app}\CaselistMaker.exe"; Tasks: desktopicon

[Run]
Filename: "{app}\CaselistMaker.exe"; Description: "{cm:LaunchProgram,Caselist Maker}"; Flags: nowait postinstall skipifsilent

[UninstallDelete]
Type: filesandordirs; Name: "{app}"