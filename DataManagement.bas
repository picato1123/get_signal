Attribute VB_Name = "DataManagement"
Option Explicit

Public Sub OutputSignal_py()
    On Error GoTo Error_Handing
    '�ϐ���`
    Dim date_from As String '�擾���t�J�n��
    Dim date_to As String   '�擾���t�I����
    Dim obj_wsh As Object   'WshShell�I�u�W�F�N�g
    Dim obj_exec As Object  'Exec�I�u�W�F�N�g
    Dim file_path As String 'python�X�N���v�g�̃t�@�C���p�X
    Dim output_signal       '�X�N���v�g���ʂ̕Ԃ�l

    '���t�w�菈��
    date_from = Format(DateAdd("d", -10, Date), "dd/mm/yyyy")
    date_to = Format(DateAdd("d", 0, Date), "dd/mm/yyyy")
    Debug.Print "DateFrom is " & date_from & vbCrLf & "DateTo is " & date_to
        
    '�X�N���v�g���s����
    file_path = ThisWorkbook.Path & "\get_signal.py"
    Set obj_wsh = CreateObject("WScript.Shell")
    Set obj_exec = obj_wsh.Exec("py " & file_path & " " & date_from & " " & date_to)
    
    '�������s�̃X�e�[�^�X�Ď�����
    Do While obj_exec.Status = 0
        DoEvents
    Loop
    
    '�Ԃ�l����
    output_signal = obj_exec.StdOut.ReadAll
    Debug.Print output_signal
    '����̃Z���ɃV�O�i����\��
    Range("G4") = output_signal
    
    Set obj_wsh = Nothing
   
    Exit Sub
    
'�G���[����
Error_Handing:
    Output_Log_File ("OutputSignal_py" & vbTab & "���s���G���[ '" & Err.Number & "'" & vbTab & Err.Description)
   
End Sub

