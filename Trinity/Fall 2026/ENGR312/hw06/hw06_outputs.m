% hw06_outputs.m

clear; clc;
format short; format compact;          
feature('hotlinks', 'off');            

root   = pwd;
srcDir = fullfile(root, 'matlab');
outDir = fullfile(root, 'outputs');
if ~exist(outDir, 'dir'); mkdir(outDir); end

scripts = dir(fullfile(srcDir, '*.m'));
for k = 1:numel(scripts)
    [~, name] = fileparts(scripts(k).name);
    outFile = fullfile(outDir, [name '.txt']);
    if exist(outFile, 'file'); delete(outFile); end   

    clearvars -except root srcDir outDir scripts k name outFile
    diary(outFile);
    run(fullfile(srcDir, scripts(k).name));
    diary off
end

feature('hotlinks', 'on');
fprintf('Ran %d scripts, outputs in %s\n', numel(scripts), outDir);
