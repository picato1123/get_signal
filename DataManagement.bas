Attribute VB_Name = "DataManagement"
Option Explicit

Public Sub OutputSignal_py()
    On Error GoTo Error_Handing
    '変数定義
    Dim date_from As String '取得日付開始日
    Dim date_to As String   '取得日付終了日
    Dim obj_wsh As Object   'WshShellオブジェクト
    Dim obj_exec As Object  'Execオブジェクト
    Dim file_path As String 'pythonスクリプトのファイルパス
    Dim output_signal       'スクリプト結果の返り値

    '日付指定処理
    date_from = Format(DateAdd("d", -10, Date), "dd/mm/yyyy")
    date_to = Format(DateAdd("d", 0, Date), "dd/mm/yyyy")
    Debug.Print "DateFrom is " & date_from & vbCrLf & "DateTo is " & date_to
        
    'スクリプト実行処理
    file_path = ThisWorkbook.Path & "\get_signal.py"
    Set obj_wsh = CreateObject("WScript.Shell")
    Set obj_exec = obj_wsh.Exec("py " & file_path & " " & date_from & " " & date_to)
    
    '同期実行のステータス監視処理
    Do While obj_exec.Status = 0
        DoEvents
    Loop
    
    '返り値処理
    output_signal = obj_exec.StdOut.ReadAll
    Debug.Print output_signal
    '所定のセルにシグナルを表示
    Range("G4") = output_signal
    
    Set obj_wsh = Nothing
   
    Exit Sub
    
'エラー処理
Error_Handing:
    Output_Log_File ("OutputSignal_py" & vbTab & "実行時エラー '" & Err.Number & "'" & vbTab & Err.Description)
   
End Sub

