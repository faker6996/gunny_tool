[Setup]
AppName=Gunny_tool
AppVersion=1.0.0
DefaultDirName={localappdata}\Gunny_tool
PrivilegesRequired=none
DefaultGroupName=Gunny_tool
UninstallDisplayIcon={app}\main.exe
OutputDir=.\Installer
OutputBaseFilename=Gunny_tool_Setup
Compression=lzma
SolidCompression=yes

[Files]
Source: "D:\Projects\python\gunny_tool\dist\main.exe"; DestDir: "{app}"; Flags: ignoreversion

[Icons]
Name: "{group}\Gunny_tool"; Filename: "{app}\main.exe"
Name: "{commondesktop}\Gunny_tool"; Filename: "{app}\main.exe"; Tasks: desktopicon

[Tasks]
Name: "desktopicon"; Description: "Tạo biểu tượng ngoài màn hình desktop"; GroupDescription: "Tùy chọn thêm:"

[Run]
Filename: "{app}\main.exe"; Description: "Khởi động ứng dụng sau khi cài"; Flags: nowait postinstall skipifsilent runascurrentuser

[UninstallDelete]
Type: filesandordirs; Name: "{app}"
