function printConfusionmatrix(truths,preds)
    % Prints Confusion Matrix given predictions and truth values
    % by Aditya S Murthy, Paridhi Srivastava and  Vatsala Singh, RIT
    
    labels=unique(truths); % find unique labels
    mat=zeros([length(labels) length(labels)]); % initialise matrix
    for k=1:length(truths) % increment indices
        i=find(labels==truths(k));
        j=find(labels==preds(k));
        mat(i,j)=mat(i,j)+1;
    end
    
    [rw, cl] = size(mat); % print in correct format
    for i=1:length(labels)
        fprintf('\t\t%d',labels(i))
    end
    
    fprintf('\n')
    
    for i=1:rw
        fprintf('%d',labels(i))
        for j=1:cl
            fprintf('\t\t%d',mat(i,j))
        end
        fprintf('\n')
    end
    
end
            