%% NSGA -  II
clear all
close all
%% Initial Parents
SS = 4;%state size
N = 20;%population size
v = [rand(N,1)*(80-40) + 40,rand(N,1)*(25-10) + 10,rand(N,1)*(13-8) + 8,rand(N,1)*(5-1) + 1];
%Initialize first random parent population

for i = 1:N
    %fitness test for each individual in the population (optimise bend angle and weight)
    [bending_angle,pressure]  = RUN_ABAQUS_BELLOW_VJ(v(i,:));
%    weight = rand(1,1);
%    stiff = rand(1,1);    
    F1(i) = bending_angle; F2(i) = pressure;
end
F1save = F1;F2save = F2; %resave fitness for later use
MF1 = (F1-(min(F1))) ./ (max(F1)-(min(F1)));MF2 = (F2-(min(F2))) ./ (max(F2)-(min(F2)));%scale fitness 0 to 1
figure(1);clf;
plot(F1,F2,'o')%plot first fitness
drawnow

%% G1 Non-dominated sort
Pp = 0;%intailize Pp which will hold the indexes of S by front 
count = 1;
while length(Pp) < N %end loop when Pp has all values
    for i = 1:N %going to run through all values of S to find front i
        if i == 1 %need to do this because P is cleared after ech fron is found since one front could be longe then another
            P = 1;
        else
            P = [P i]; %add next index to P to be tested
            for j = 1:length(P)
                if length(P)~=j
                if F1(P(length(P))) >= F1(P(j)) && F2(P(length(P))) >= F2(P(j)) || F1(P(length(P))) <= F1(P(j)) && F2(P(length(P))) <= F2(P(j))

                    %nondominated (in this program I want to minimize F1 and Maximize F2 which is why the statements are the way they are)
                    % do nothing
                elseif F1(P(length(P))) < F1(P(j)) && F2(P(length(P))) > F2(P(j))%dominating
                    A = exist('d');
                    if A == 0
                        d = j;
                    else
                        d = [d j];
                    end
                elseif F1(P(length(P))) > F1(P(j)) && F2(P(length(P))) < F2(P(j))%dominated
                    P(length(P)) = [];
                    clear d
                    break
                end
                end
            end
            %if current individual dominates others delete the others
            A = exist('d');
            if A > 0
            for k = 1:length(d)    
                P(d(k)+1-k) = [];
            end
            end
            clear d;
            
        end
    end
    %output is P which hold the indexes of given front 
    %First lets rank P based on F1 decneding thus F2 asending
    [F1sort,inPwF1] = sort(F1(P),'descend');
    P = P(inPwF1);

    %add front to Pp
    if Pp == 0
        Pp = [P;F1(P);F2(P);ones(1,length(P))];%
    else
        Pp = [Pp [P;F1(P);F2(P);(count*ones(1,length(P)))]];%
    end

    %remove Pp from list to look through
    for K = 1:length(P)
        F1(P(K)) = 100000; %F1 is being minimized
        F2(P(K)) = -100000; %F2 is being maximized
    end
    %set fronts for booking keeping and later use
    if i > 1
    for L = 1:length(P)
        Fronts(count,L) = P(L);
    end
    end
    count = count +1;
    clear P
    %F1;F2;Pp;pause
end
%Pp now contains index's in order with corresponding fronts and fitnesses 
%but not crowding distance


%% G1 corwding distance
[Z,X] = size(Fronts);c = 1;
for i = 1:Z
    CurFr = nonzeros(Fronts(i,:))';
    %calculate crouding distance
        
    if length(CurFr)==1%one individual in front
        cwdis(1) = 1000;
        c = c+1;
    elseif length(CurFr) == 2%two individual in front
        cwdis(1) = 1000;
        cwdis(2) = 1000;
        c = c+2;
    elseif length(CurFr)>2 %assign crowding distance values if front is larger than 2 individuals
        cwdis(1) = 100;
        cwdis(length(CurFr)) = 1000;
        for g = 2:length(CurFr)-1
            cwdis(g) = MF1(CurFr(g-1))+MF1(CurFr(g+1))  +  MF2(CurFr(g-1))+MF2(CurFr(g+1)); 
        end
        c = c+length(CurFr);
    end
    if i == 1
        density = cwdis;
    else
        density = [density cwdis];
    end
    
    clear CurFr
    clear cwdis
end
% put crowding dis into Pp, now has index, front, fitness, and crowding dis
Pp = [Pp' density']';

Q = 0;I = 0;
%% G1 tournement selection recombination and mutation
while I < N
    %Select two parents
    Icom1 = datasample([1:N],1);
    Icom2 = datasample([1:N],1);
    Icom3 = datasample([1:N],1);
    Icom4 = datasample([1:N],1);
    if Pp(4,Icom1) > Pp(4,Icom2)
        Ipar1 = Icom1;
    elseif Pp(4,Icom1) < Pp(4,Icom2)
        Ipar1 = Icom2;
    elseif Pp(4,Icom1) == Pp(4,Icom2)
        if Pp(5,Icom1) < Pp(5,Icom2)
            Ipar1 = Icom2;
        elseif Pp(5,Icom1) > Pp(5,Icom2)
            Ipar1 = Icom1;
        elseif Pp(5,Icom1) == Pp(5,Icom2)
            Ipar1 = Icom1;
        end
    end
    
    if Pp(4,Icom3) > Pp(4,Icom4)
        Ipar2 = Icom3;
    elseif Pp(4,Icom3) < Pp(4,Icom4)
        Ipar2 = Icom4;
    elseif Pp(4,Icom3) == Pp(4,Icom4)
        if Pp(5,Icom3) < Pp(5,Icom4)
            Ipar2 = Icom4;
        elseif Pp(5,Icom3) > Pp(5,Icom4)
            Ipar2 = Icom3;
        elseif Pp(5,Icom3) == Pp(5,Icom4)
            Ipar2 = Icom3;
        end
    end
    % cross two parents and mutate to get Q
    % choose crossing point
    crosspoint = rand(1);
    crosspoint = round(crosspoint*SS);

    s(1:crosspoint) = v(Ipar1,(1:crosspoint));
    s(crosspoint+1:SS) = v(Ipar2,(crosspoint+1:SS));
    
    mutation = rand(1,1);
    posneg = rand(1,1);
    mutationloc = round(rand(1,1)*9)+1;
    if posneg >= 0.5
        s(mutationloc) = s(mutationloc)-mutation;
    else
        s(mutationloc) = s(mutationloc)+mutation;
    end
    
    if Q == 0
        Q = s';
    else
        Q = [Q s'];
    end
    [U,I] = size(Q);
end

thickmax = 5.0;
thickmin = 0.1;
idmax = 20.0;
idmin = 0.5;
id = Q(1:5,:);
thick = Q(6:10,:);

id(id>idmax) = idmax;
id(id<idmin) = idmin;
thick(thick>thickmax) = thickmax;
thick(thick<thickmin) = thickmin;
%Clip to xMax
Q = [id;thick];
Q = Q'; S = v;

%pause

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%% NSGA-II Main loop %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% 
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%% GN fitness
for loopcount = 1:300
R = [S' Q']';%merge parent and child populations
%pause
for i = N+1:2*N
    [stiff,weight]  = RUN_ABAQUS_BELLOW(R(i,:));
    F1(i) = stiff;
    F2(i) = weight;
end
%F1 = (R(1,:).*cos(R(1,:).*(R(2,:)+R(3,:))))+R(1,:);
%F2 = 1+exp(-R(1,:));
F1save = F1;
F2save = F2;
MF1 = (F1-(min(F1))) ./ (max(F1)-(min(F1)));
MF2 = (F2-(min(F2))) ./ (max(F2)-(min(F2)));

%run NDS to put in fronts
clear Fronts;
clear d;
clear Pp;
Pp = 0;
count = 1;

while length(Pp) < 2*N %end loop when Pp has all values

for i = 1:2*N %going to run through all values of S to find front i
    if i == 1 %need to do this because P is cleared after ech fron is found since one front could be longe then another
        P = 1;
    else
        P = [P i]; %add next index to P to be tested
            for j = 1:length(P)
                if length(P)~=j
                if F1(P(length(P))) >= F1(P(j)) && F2(P(length(P))) >= F2(P(j)) || F1(P(length(P))) <= F1(P(j)) && F2(P(length(P))) <= F2(P(j))

                    %nondominated (in this program I want to minimize F1 and Maximize F2 which is why the statements are the way they are)
                    % do nothing
                elseif F1(P(length(P))) < F1(P(j)) && F2(P(length(P))) > F2(P(j))%dominating
                    A = exist('d');
                    if A == 0
                        d = j;
                    else
                        d = [d j];
                    end
                elseif F1(P(length(P))) > F1(P(j)) && F2(P(length(P))) < F2(P(j))%dominated
                    P(length(P)) = [];
                    clear d
                    break
                end
                end
            end
        A = exist('d');
        if A > 0
        for k = 1:length(d)    
            P(d(k)+1-k) = [];
        end
        end
        clear d;
        %d = 0;
    end
end

%output is P which fold the indexes of given front with out any other
%information

%First lets rank P based on F1

[F1sort,inPwF1] = sort(F1(P),'descend');
P = P(inPwF1);
% F1givcurfr =

%Now P is list of indexes in given front in descending order with respect to F1 

%add front to Pp
if Pp == 0
    Pp = [P;F1(P);F2(P);ones(1,length(P))];%
else
    Pp = [Pp [P;F1(P);F2(P);(count*ones(1,length(P)))]];%
end

%remove Pp from 
for K = 1:length(P)
    F1(P(K)) = 1000000;
    F2(P(K)) = -1000000;
end
if i > 1
for L = 1:length(P)
    Fronts(count,L) = P(L);
end
end
count = count +1;
clear P
%F1;F2;Pp;pause
end


%calculate crowding thing
c = 1;
[Z,X] = size(Fronts);
for i = 1:Z
    CurFr = nonzeros(Fronts(i,:))';
    %calculate crouding distance
       

    
    if length(CurFr)==1
        cwdis(1) = 100+rand(1);
        c = c+1;
    elseif length(CurFr) == 2
        %you don't know that 1 and L are the max and min, you munst first
        %find that
        cwdis(1) = 100+rand(1);
        cwdis(2) = 100+rand(1);
        c = c+2;
    elseif length(CurFr)>2
        cwdis(1) = 100+rand(1);
        cwdis(length(CurFr)) = 100+rand(1);
        for g = 2:length(CurFr)-1
            cwdis(g) = MF1(CurFr(g-1))+MF1(CurFr(g+1))  +  MF2(CurFr(g-1))+MF2(CurFr(g+1));
        end
        c = c+length(CurFr);
    end
    if i == 1
        density = cwdis;
    else
        density = [density cwdis];
    end
    
    clear CurFr
    clear cwdis
end
% put crowding dis into Pp
Pp = [Pp' density']';

%Need to sort Pp
clear index
index = 0;
cou = 1;
for i=1:Z
    CurFr = nonzeros(Fronts(i,:))';
    L = length(CurFr);
    [val,ii] = sort(Pp(5,cou:cou+L-1),'descend');
    if index == 0
        index = ii;
    else
        index = [index ii+cou-1];
    end
    cou =cou+L;
end

Pp(1,:) = Pp(1,index);
Pp(2,:) = Pp(2,index);
Pp(3,:) = Pp(3,index);
Pp(4,:) = Pp(4,index);
Pp(5,:) = Pp(5,index);


%%%%%%%%%NEEDS fixing%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

for sam = 1:SS
R(:,sam) = R(Pp(1,:),sam);
end
% R(2,:) = R(2,Pp(1,:));
% R(3,:) = R(3,Pp(1,:));

%cut top N 
%Need Pp and S from cut population
 Pp = Pp(:,1:end-N);
 S = R(1:end-N,:);
 clear F1; clear F2; clear MF1; clear MF2;
 F1 = F1save(Pp(1,:));
 F1 = F1(:,1:end-N);
 F2 = F2save(Pp(1,:));
 F2 = F2(:,1:end-N);
%  F1 = (S(1,:).*cos(S(1,:).*(S(2,:)+S(3,:))))+S(1,:);
% F2 = 1+exp(-S(1,:));
MF1 = (F1-(min(F1))) ./ (max(F1)-(min(F1)));
MF2 = (F2-(min(F2))) ./ (max(F2)-(min(F2)));
figure(1)
clf;
plot(F1,F2,'o')
xlim([-15 20])
ylim([-1 160])
drawnow

%create children
clear Q
Q = 0;I = 1;
%tournement selection recombination and mutation
while I < N
    %Select two parents
    Icom1 = datasample([1:N],1);
    Icom2 = datasample([1:N],1);
    Icom3 = datasample([1:N],1);
    Icom4 = datasample([1:N],1);
    if Pp(4,Icom1) > Pp(4,Icom2)
        Ipar1 = Icom1;
    elseif Pp(4,Icom1) < Pp(4,Icom2)
        Ipar1 = Icom2;
    elseif Pp(4,Icom1) == Pp(4,Icom2)
        if Pp(5,Icom1) < Pp(5,Icom2)
            Ipar1 = Icom2;
        elseif Pp(5,Icom1) > Pp(5,Icom2)
            Ipar1 = Icom1;
        elseif Pp(5,Icom1) == Pp(5,Icom2)
            Ipar1 = Icom1;
        end
    end
    
    if Pp(4,Icom3) > Pp(4,Icom4)
        Ipar2 = Icom3;
    elseif Pp(4,Icom3) < Pp(4,Icom4)
        Ipar2 = Icom4;
    elseif Pp(4,Icom3) == Pp(4,Icom4)
        if Pp(5,Icom3) < Pp(5,Icom4)
            Ipar2 = Icom4;
        elseif Pp(5,Icom3) > Pp(5,Icom4)
            Ipar2 = Icom3;
        elseif Pp(5,Icom3) == Pp(5,Icom4)
            Ipar2 = Icom3;
        end
    end
    % cross two parents and mutate to get Q
    % choose crossing point
    crosspoint = rand(1);
    crosspoint = round(crosspoint*SS);

    s(1:crosspoint) = v(Ipar1,(1:crosspoint));
    s(crosspoint+1:SS) = v(Ipar2,(crosspoint+1:SS));
    
     mutation = rand(1,1);
    posneg = rand(1,1);
    mutationloc = round(rand(1,1)*9)+1;
    if posneg >= 0.5
        s(mutationloc) = s(mutationloc)-mutation;
    else
        s(mutationloc) = s(mutationloc)+mutation;
    end
    
    %Create new vector for Q
    
    if Q == 0
        Q = s';
    else
        Q = [Q s'];
    end
    [U,I] = size(Q);
end

%% Set limits on values
thickmax = 5.0;
thickmin = 0.1;
idmax = 20.0;
idmin = 0.5;
id = Q(1:5,:);
thick = Q(6:10,:);

id(id>idmax) = idmax;
id(id<idmin) = idmin;
thick(thick>thickmax) = thickmax;
thick(thick<thickmin) = thickmin;
%Clip to xMax
Q = [id;thick];
Q = Q';
loopcount
end
%check loop number


% %sort fittness F1 might be unneeded
% [SF1,I1] = sort(F1); % you don't truely care about hte F at this point just the index which relates back to the state vector
% SSF1(1,:) = S(1,I1);
% SSF1(2,:) = S(2,I1);
% SSF1(3,:) = S(3,I1);
% %sort fittness F2
% [SF2,I2] = sort(F2);
% SSF2(1,:) = S(1,I2);
% SSF2(2,:) = S(2,I2);
% SSF2(3,:) = S(3,I2);

% S vectors are now in ranked order is now in ranked order


    %Resort CurFr in order of acending F1 and F2
%     for u = 1:length(CurFr)
% %         clear fitval
% %         fitval = 0;
%     fitval = F1(CurFr(u)); 
%     %F2(CurFr(1)) = fitness 2 of index one in current front
%     if u == 1
%         Curfit = fitval;
%     else
%         Curfit = [Curfit fitval];
%     end
%     end
%     %Get those fitness values and sort them, also save index
%     [RCurfit,inrf] = sort(Curfit);
%     %sort CurFr based on sorted F1 values
%     CurFr = CurFr(inrf);





%run NDS to put in fronts
% clear Fronts;
% clear d;
% clear Pp;
% Pp = 0;
% count = 1;
% while length(Pp) < 2*N
% 
% for i = 1:length(R)
%     if i == 1
%         P = 1;
%     else
%         P = [P i];
%         for j = 1:length(P)
%             if length(P)~=j
%             if F1(P(length(P))) <= F1(P(j)) && F2(P(length(P))) >= F2(P(j)) || F1(P(length(P))) >= F1(P(j)) && F2(P(length(P))) <= F2(P(j))   
%                 % do nothing
%             elseif F1(P(length(P))) > F1(P(j)) && F2(P(length(P))) > F2(P(j))
%                 A = exist('d');
%                 if A == 0
%                     d = j;
%                 else
%                     d = [d j];
%                 end
%             %elseif F1(i) <= F1(j) && F2(i) >= F2(j) || F1(i) >= F1(j) && F2(i) <= F2(j)
%                 %neither is dominated so leave both in ie do nothing, might be
%                 %a worthless check
%                 
%             elseif F1(P(length(P))) < F1(P(j)) && F2(P(length(P))) < F2(P(j))
%                 %delete P(i) and end inner loop
% %                 j = length(P);
%                 P(length(P)) = [];
%                 clear d
%                 break
%             end
%             end
%         end
%         A = exist('d');
%         if A > 0
%         for k = 1:length(d)    
%             P(d(k)+1-k) = [];
%         end
%         end
%         clear d;
%     end
% end
% 
% %add front to Pp
% if Pp == 0
%     Pp = [P;ones(1,length(P))];
% else
%     Pp = [Pp [P;(count*ones(1,length(P)))]];
% end
% 
% 
% 
% %remove Pp from 
% for K = 1:length(P)
%     F1(P(K)) = -100;
%     F2(P(K)) = -100;
% end
% if i > 1
% for L = 1:length(P)
%     Fronts(count,L) = P(L);
% end
% end
% count = count +1;
% clear P
% %F1;F2;Pp;pause
% end
