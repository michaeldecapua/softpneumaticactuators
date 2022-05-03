function [F1,F2] =  RUN_ABAQUS_BELLOW_VJ(state)
%function [F1,F2] =  RUN_ABAQUS_BELLOW_VJ()

% state(1) = rand(1)*(80-40) + 40;
% state(2) = rand(1)*(25-10) + 10;
% state(3) = rand(1)*(13-8) + 8;
% state(4) = rand(1)*(5-1) + 1;
% %Variables
%mo='noGUI';
mo='script';

%Make python file with variables
delete('abaqus.rpt');delete('python_file_rev1.prt');delete('python_file_rev1.odb');delete('python_file_rev1.msg');delete('python_file_rev1.log');delete('python_file_rev1.imp');delete('python_file_rev1.inp');delete('python_file_rev1.dat');delete('python_file_rev1.com');
delete('Vara_VJ.py');

pressure = 0.01;
A1 = state(4)*12;
F = pressure*A1;
Atot = state(2)*20;
A2 = Atot-A1;
Force  = F/A2;

fid = fopen('Vara_VJ.py', 'w');
for i = 1:length(state)
fprintf(fid,'state%d = %0.4f\n',i,state(i));
end
%variables file is changed by MATLAB

fprintf(fid,'pressure = %0.4f\n',pressure);
%fprintf(fid,'force = %0.4f\n',Force);
fclose(fid);

%Make part(run Abaqus)
unix(['abaqus cae ',mo,'=python_file_rev1.py','&&']);
%calls the main python file, which used the updated variable file and runs
%the abaqus simulation

%Unix system   %system(['abaqus cae ',mo,'=Main_full.py','&']); %Windows system

w = exist('abaqus_VJ.rpt');
while w == 0
    %wait for sim to finish
    w = exist('abaqus_VJ.rpt');
end
pause(1);
import java.awt.Robot;
import java.awt.event.*;
mouse = Robot;
mouse.mouseMove(0,0);
%screenSize = get(0,'screensize');
mouse.mouseMove(1900,10);
mouse.mouseMove(1900,10);
mouse.mouseMove(1900,10);
mouse.mouseMove(1900,10);
mouse.mousePress(InputEvent.BUTTON1_MASK);
mouse.mouseRelease(InputEvent.BUTTON1_MASK);

mouse.mouseMove(0,0);
mouse.mouseMove(1225,1050);
mouse.mouseMove(1225,1050);
mouse.mouseMove(1225,1050);
mouse.mouseMove(1225,1050);
mouse.mouseMove(1225,1050);
mouse.mouseMove(1225,1050);
mouse.mousePress(InputEvent.BUTTON3_MASK);
mouse.mouseRelease(InputEvent.BUTTON3_MASK);
pause(1)
mouse.mouseMove(1225,1000);
mouse.mouseMove(1225,1000);
mouse.mouseMove(1225,1000);
mouse.mouseMove(1225,1000);
mouse.mouseMove(1225,1000);
mouse.mouseMove(1225,1000);
mouse.mousePress(InputEvent.BUTTON1_MASK);
mouse.mouseRelease(InputEvent.BUTTON1_MASK);

filetext = fileread('abaqus_VJ.rpt');

F1 = str2double(regexp(filetext, '(?<=Total[^0-9]*)[0-9]*\.?[0-9]+', 'match'));
if F1 <10
    l = sprintf('(?<=Total     %.5fE-0[^0-9]*)[0-9]*\\.?[0-9]+', F1);
    numbers1 = str2double(regexp(filetext, l, 'match'));
    l = sprintf('(?<=Total     %.5fE-0%d[^0-9]*)[0-9]*\\.?[0-9]+', F1,numbers1);
    F2 = str2double(regexp(filetext, l, 'match'));
elseif F1 <100
    l = sprintf('(?<=Total     %.4fE-0[^0-9]*)[0-9]*\\.?[0-9]+', F1);
    numbers1 = str2double(regexp(filetext, l, 'match'));
    l = sprintf('(?<=Total     %.4fE-0%d[^0-9]*)[0-9]*\\.?[0-9]+', F1,numbers1);
    F2 = str2double(regexp(filetext, l, 'match'));
elseif F1 >100
    l = sprintf('(?<=Total     %.3fE-0[^0-9]*)[0-9]*\\.?[0-9]+', F1);
    numbers1 = str2double(regexp(filetext, l, 'match'));
    l = sprintf('(?<=Total     %.3fE-0%d[^0-9]*)[0-9]*\\.?[0-9]+', F1,numbers1);
    F2 = str2double(regexp(filetext, l, 'match'));
end 
if isempty(F2)
    if F1 <10
        l = sprintf('(?<=Total    -%.5fE-0[^0-9]*)[0-9]*\\.?[0-9]+', F1);
        numbers1 = str2double(regexp(filetext, l, 'match'));
        l = sprintf('(?<=Total    -%.5fE-0%d[^0-9]*)[0-9]*\\.?[0-9]+', F1,numbers1);
        F2 = str2double(regexp(filetext, l, 'match'));
    elseif F1 <100
        l = sprintf('(?<=Total    -%.4fE-0[^0-9]*)[0-9]*\\.?[0-9]+', F1);
        numbers1 = str2double(regexp(filetext, l, 'match'));
        l = sprintf('(?<=Total    -%.4fE-0%d[^0-9]*)[0-9]*\\.?[0-9]+', F1,numbers1);
        F2 = str2double(regexp(filetext, l, 'match'));
    elseif F1 >100
        l = sprintf('(?<=Total    -%.3fE-0[^0-9]*)[0-9]*\\.?[0-9]+', F1);
        numbers1 = str2double(regexp(filetext, l, 'match'));
        l = sprintf('(?<=Total    -%.3fE-0%d[^0-9]*)[0-9]*\\.?[0-9]+', F1,numbers1);
        F2 = str2double(regexp(filetext, l, 'match'));
    end 
end
if isempty(F2)
    if F1 <10
        l = sprintf('(?<=Total    -%.5fE-1[^0-9]*)[0-9]*\\.?[0-9]+', F1);
        numbers1 = str2double(regexp(filetext, l, 'match'));
        l = sprintf('(?<=Total    -%.5fE-1%d[^0-9]*)[0-9]*\\.?[0-9]+', F1,numbers1);
        F2 = str2double(regexp(filetext, l, 'match'));
    elseif F1 <100
        l = sprintf('(?<=Total    -%.4fE-1[^0-9]*)[0-9]*\\.?[0-9]+', F1);
        numbers1 = str2double(regexp(filetext, l, 'match'));
        l = sprintf('(?<=Total    -%.4fE-1%d[^0-9]*)[0-9]*\\.?[0-9]+', F1,numbers1);
        F2 = str2double(regexp(filetext, l, 'match'));
    elseif F1 >100
        l = sprintf('(?<=Total    -%.3fE-1[^0-9]*)[0-9]*\\.?[0-9]+', F1);
        numbers1 = str2double(regexp(filetext, l, 'match'));
        l = sprintf('(?<=Total    -%.3fE-1%d[^0-9]*)[0-9]*\\.?[0-9]+', F1,numbers1);
        F2 = str2double(regexp(filetext, l, 'match'));
    end 
end
if isempty(F2)
    if F1 <10
        l = sprintf('(?<=Total     %.5fE-1[^0-9]*)[0-9]*\\.?[0-9]+', F1);
        numbers1 = str2double(regexp(filetext, l, 'match'));
        l = sprintf('(?<=Total     %.5fE-1%d[^0-9]*)[0-9]*\\.?[0-9]+', F1,numbers1);
        F2 = str2double(regexp(filetext, l, 'match'));
    elseif F1 <100
        l = sprintf('(?<=Total     %.4fE-1[^0-9]*)[0-9]*\\.?[0-9]+', F1);
        numbers1 = str2double(regexp(filetext, l, 'match'));
        l = sprintf('(?<=Total     %.4fE-1%d[^0-9]*)[0-9]*\\.?[0-9]+', F1,numbers1);
        F2 = str2double(regexp(filetext, l, 'match'));
    elseif F1 >100
        l = sprintf('(?<=Total     %.3fE-1[^0-9]*)[0-9]*\\.?[0-9]+', F1);
        numbers1 = str2double(regexp(filetext, l, 'match'));
        l = sprintf('(?<=Total     %.3fE-1%d[^0-9]*)[0-9]*\\.?[0-9]+', F1,numbers1);
        F2 = str2double(regexp(filetext, l, 'match'));
    end 
end