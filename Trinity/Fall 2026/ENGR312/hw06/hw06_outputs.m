% hw06_outputs.m
% Runs each problem script in matlab/ and saves its Command Window output
% to outputs/<name>.txt. ENGR312HW6.tex lists both the script and its
% output with \lstinputlisting, so editing a script and rerunning this
% keeps the code and output in the PDF in sync.
%
% Run from the folder that holds ENGR312HW6.tex:   >> hw06_outputs

clear; clc;
format short; format compact;          % compact drops the blank lines between results
feature('hotlinks', 'off');            % keeps hyperlink markup out of the saved text (undocumented, widely used)

root   = pwd;
srcDir = fullfile(root, 'matlab');
outDir = fullfile(root, 'outputs');
if ~exist(outDir, 'dir'); mkdir(outDir); end

scripts = dir(fullfile(srcDir, '*.m'));
for k = 1:numel(scripts)
    [~, name] = fileparts(scripts(k).name);
    outFile = fullfile(outDir, [name '.txt']);
    if exist(outFile, 'file'); delete(outFile); end   % diary appends, so start clean

    clearvars -except root srcDir outDir scripts k name outFile
    diary(outFile);
    run(fullfile(srcDir, scripts(k).name));
    diary off
end

feature('hotlinks', 'on');
fprintf('Ran %d scripts, outputs in %s\n', numel(scripts), outDir);

% Optional: compile the PDF from here if a LaTeX distribution is on your PATH
% (MiKTeX on Windows, MacTeX on macOS).
% system('pdflatex -interaction=nonstopmode ENGR312HW6.tex');
