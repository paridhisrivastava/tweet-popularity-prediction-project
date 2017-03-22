% Uses libsvm 3.18 found at http://www.csie.ntu.edu.tw/~cjlin/libsvm to perform classifications
% by Aditya S Murthy, Paridhi Srivastava and  Vatsala Singh, RIT

tic
d=importdata('TrainingData.csv'); % separate training data and labels
data=d.data;
traininst=data(:,1:14);
trainrpop=data(:,16);
trainfpop=data(:,18);

f=importdata('TestData.csv'); % separate testing data and labels
data=f.data;
testinst=data(:,1:14);
testrpop=data(:,16);
testfpop=data(:,18);

totdata=[traininst;testinst]; % perform scaling and separate again
maxx=max(totdata);
minn=min(totdata);
scaledtotdata=scalemaxmin(totdata,maxx,minn);
[m,n]=size(scaledtotdata);
traininstdata=scaledtotdata(1:15383,:);
testinstdata=scaledtotdata(15384:m,:);

disp('Labelling based on retweets')
% uncomment these lines to retrain
% opt=['-q -h 0 -t 2 -c ',num2str(2^5), ' -g ' , num2str(2^2)]; 
% disp('Training...')
% mod1 = svmtrain(trainrpop, traininstdata, opt);% train using best parameters
% save('model1','mod1')
load('model1')
disp('Testing..')
[ preds] = svmpredict(testrpop, testinstdata, mod1); 
disp(sum(preds==testrpop)/length(preds));
printConfusionmatrix(testrpop,preds)

disp('Labelling based on favourites')
% uncomment these lines to retrain
% opt=['-q -h 0 -t 2 -c ',num2str(2^5), ' -g ' , num2str(2^1.5)];
% disp('Training...')
% mod2 = svmtrain(trainfpop, traininstdata, opt);% train using best parameters
% save('model2','mod2')
load('model2')
disp('Testing..')
[ preds] = svmpredict(testfpop, testinstdata, mod2); 
disp(sum(preds==testfpop)/length(preds));
printConfusionmatrix(testfpop,preds)

toc


