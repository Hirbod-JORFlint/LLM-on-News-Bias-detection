%
% File acl2020.tex
%
%% Based on the style files for ACL 2020, which were
%% Based on the style files for ACL 2018, NAACL 2018/19, which were
%% Based on the style files for ACL-2015, with some improvements
%%  taken from the NAACL-2016 style
%% Based on the style files for ACL-2014, which were, in turn,
%% based on ACL-2013, ACL-2012, ACL-2011, ACL-2010, ACL-IJCNLP-2009,
%% EACL-2009, IJCNLP-2008...
%% Based on the style files for EACL 2006 by 
%%e.agirre@ehu.es or Sergi.Balari@uab.es
%% and that of ACL 08 by Joakim Nivre and Noah Smith

\documentclass[11pt,a4paper]{article}
\usepackage[hyperref]{acl2020}
\usepackage{times}
\usepackage{latexsym}
\usepackage{graphicx}
\usepackage{amsmath}
\renewcommand{\UrlFont}{\ttfamily\small}
\usepackage{microtype}

\aclfinalcopy

%\setlength\titlebox{5cm}
% You can expand the titlebox if you need extra space
% to show all the authors. Please do not make the titlebox
% smaller than 5cm (the original size); we will check this
% in the camera-ready version and ask you to change it back.

\title{Bias identification using Large Language Model}

\author{Hirbod Gholamniaetakhsami \\
  Linköping University / Linköping City \\
  \texttt{hirgh815@student.liu.se}}

\date{08 March 2024}

\begin{document}
\maketitle
\begin{abstract}
This document is a template for preparing a manuscript for the proceedings of the GermEval 2021 shared task on the identification of toxic, engaging, and fact-claiming comments. It follows the ACL 2020 proceedings template.
The document is an example of what your manuscript should look like.
\end{abstract}

\section{Introduction}

In the era of information overload, the ability to discern bias in news articles is more critical than ever. This research project aims to develop an innovative, machine learning-based approach to identify and quantify bias in news articles. The proposed methodology will involve using natural language processing techniques to analyze the linguistic patterns in the text, which often indicate a certain bias. The project contains two stages which are comprised of 1- fine-tuning a language model for the classification task of labeling the news article text and 2- evaluating the model through two methodologies. 

This project, if successful, has significant implications for the field of journalism. It can provide a tool for readers to better understand the biases in the news they consume, and for journalists and editors to more effectively check their work for unintentional bias. Ultimately, this could contribute to a more informed and discerning public discourse.
The next sections of this project is as follows:
Section two provides the necessary context and theoretical foundation for the study. It includes a literature review highlighting relevant previous work in the field of news bias, particularly the studies involving automated tools for this purpose. It also outlines the motivation for this study and states the research problem and objectives. Section three details the data, preprocessing steps, and the process of fine-tuning the RoBERTa model. It also explains the implementation of a 5-fold cross-validation strategy and the application of oversampling techniques. Section four presents the outcomes of the fine-tuning process and the performance of the model on the validation set. It includes detailed analysis and interpretation of the results, supported by appropriate statistical measures and visualizations. Any patterns, relationships, or trends observed in the results are highlighted and discussed. The final section wraps up the study by summarizing the key findings and their implications. It discusses the strengths and limitations of the current study, and how these findings contribute to the existing body of knowledge.
\section{Background}
Bias, whether intentional or unintentional, can significantly influence public opinion and discourse. Understanding the background and implications of this issue is crucial to this research. 
Essentially Bias can be categorized in many forms~\cite{mastrine_2019}, including:
\begin{itemize}
    \item Unsubstantiated Claims: These are statements that are not supported by evidence.
    \item Opinion Statements Presented as Facts: This occurs when journalists present their personal opinions as if they are objective truths.
    \item Sensationalism/Emotionalism: This involves using exciting or shocking stories, languages, or visuals at the expense of accuracy to overhype an issue and generate public curiosity.
    \item Flawed Logic: This involves using faulty reasoning to make an argument.
    \item Commission: This involves permitting errors or false assumptions that support a specific point of view.
\end{itemize}
Each of these types of bias can influence how news is reported and how audiences perceive events and issues. Therefore consumers of news need to be aware of these biases to critically evaluate the information they receive. Entman~\cite{entman_2007} signifies the importance of bias in media. The author also emphasizes the importance of understanding these biases to comprehend how media influences the distribution of power and affects democracy. In this regard based on the content the type of bias that is delivered to the audience can be described as follows:
\begin{itemize}
    \item Distortion Bias: This refers to news that allegedly distorts or falsifies reality.
    \item Content Bias: News that favors one side in a political conflict over another, rather than providing equivalent treatment to both sides.
    \item Decision-Making Bias: Biases related to the motivations and mindsets of journalists who produce the content.
\end{itemize}
The significant influence of media on society and the responsibility of avoiding biased content is undeniable. ~\cite{chen_khalid al khatib_wachsmuth_stein_2020} presents a methodology for automatic political bias detection. The dataset utilized in this research contains a corpus of 6964 articles. The target of this analysis is the study of the distribution of bias and how it manifests at different levels of text granularity, from word to entire articles. The authors further reveal some common patterns of bias at various text levels, noting that the last part of an article tends to be the most biased.\\
Deductive Content Analysis is a common method used in qualitative studies to interpret and analyze data~\cite{graneheim_lindgren_lundman_2017}. Such social media models have been used for decades in the field of media bias analysis.~\cite{hamborg_zhukova_gipp_2019} combines manual inspection methods from social sciences with natural language processing techniques. The authors introduced an automated identification of Media Bias by word choice and labeling in news articles. This approach involves extracting potential instances of bias, merging similar semantic concepts, and analyzing the framing of these instances to reveal bias. It is shown to achieve an F1 score of 45.7\% which can be described as one of the best-performing models outside of machine learning approaches.\\
There are various research on how to detect media bias effectively.
~\cite{benson_cruickshank_2024} developed a method to cluster cable news programs based on their biases. By analyzing the topics discussed (using Named Entity Recognition) and how they are discussed (through Stance Analysis), programs with similar biases were grouped.\\
~\cite{wu_liu_xu_wu_2022} proposed a novel to mitigate biases in evidence-based fake news detection. The causal intervention is used as a means to mitigate biases that are introduced during the data collection phase. As a model-agnostic method, it can be applied to various models for fake news detection. Additionally, the framework has shown promise in improving the robustness of augmented models.\\
~\cite{hu_chen_yin_nie_2022} shows another application of causal inference on fake news detection. In this article, a novel framework(CLIMB) for multi-modal fake news detection was introduced. This approach addresses the problem of image-text matching bias in fake news detection. The task of fake news detection was formulated as a causal graph to reflect cause-effect factors. It has been shown that this model effectively improves fake news detection on real-world datasets.\\
~\cite{arruda_roman_monteiro_2020} proposed a tripartite model to analyze three types of bias: Selection bias, coverage bias, and statement bias. Assuming the bias is a deviation from the mainstream behavior, the authors introduce an outlier detection framework to gain insight into the existence and their nature in media outlets. Despite the inherent limitation of their proposed methodology, it shows promise to identify specific biases.
~\cite{dmansouri_naderan-tahan_rashti_2020} discusses a semi-supervised learning method for detecting fake news in social media using a novel deep learning technique called SLD-CNN. This method combines convolutional neural networks(CNNs) with Linear Discriminant Analysis (LDA) for complex feature extraction and class separation respectively. As a method usable for both labeled and unlabeled data, this approach is especially useful in case of real-world application and data scarcity.\\
Subjective bias can significantly impact the validity and reliability of research findings, leading to distorted results and wrong conclusions. ~\cite{pryzant_diehl_martinez_dass_kurohashi_jurafsky_yang_2020} aims to address the issue of subjective bias in texts that are expected to be objective such as news articles. The authors propose two encoder-decoder baseline algorithms for this task. In this paper, a human evaluation of four domains of encyclopedias, news headlines, books, and political speeches shows that both proposed algorithms are capable of reducing bias in texts.\\
To summarize the literature revolving around news bias detection and identification of fake news involves one or more than the following steps:
\begin{itemize}
    \item Bias detection: To detect whether a news article is biased or not.
    \item Bias recognition: To recognize the biased words or phrases from the news articles.
    \item De-biasing: To de-bias the data by replacing the biased words or phrases from the news article with unbiased or at least less biased word(s).
\end{itemize}
~\cite{hamborg_donnay_gipp_2018}  discusses the impact of media bias on public perception and the importance of unbiased news in shaping opinions. The authors review interdisciplinary approaches to analyzing media bias, combining social sciences and computer science methods with a focus on automated methods for identifying media bias in news articles, particularly using natural language processing (NLP).
The next two review articles ~\cite{khushi_rakhecha_simran_rauniyar_agrawal_bhatt_2023,rohera_shethna_patel_thakker_tanwar_gupta_hong_sharma_2022} provide two comprehensive surveys on news bias detection based on deep learning methods and fake news classification. The first paper reviewed a variety of deep learning models such as BERT and Long Short-Term Memory(LSTM) and Machine Learning algorithms such as logistic regression, While in the latter paper in addition to the introduction of models, authors also implemented models on a self aggregated dataset containing 6335 rows and four columns. According to the second paper, the highest accuracy belongs to the LSTM model which also shows the highest Recall. The primary reason for mentioning the task of fake news classification alongside the main focus of this project is that these tasks are highly similar and often show correlation:
\begin{enumerate}
  \item Shared Objective: Both fields aim to assess the credibility and objectivity of news content. While fake news classification focuses on distinguishing between true and false information, news bias identification seeks to determine the presence of any partiality or prejudice in the news.
  \item Similar Techniques: Both fields often employ similar computational and linguistic techniques for analysis. These include Natural Language Processing (NLP), Machine Learning (ML), and Deep Learning (DL) algorithms to analyze text and identify patterns.
  \item Interconnected Nature: The presence of bias can sometimes be a strong indicator of fake news. Biased news articles may distort facts or present misleading information, which is a characteristic of fake news. Therefore, identifying bias can be a crucial step in the process of fake news detection.
\end{enumerate}
By providing a more objective measure of bias, this research could significantly enhance the transparency of news reporting and empower readers to make more informed judgments about the news they consume. 

\section{Methods}
\subsection{Data}
The primary dataset utilized in this study is derived from the paper ‘Neural Media Bias Detection Using Distant Supervision With BABE - Bias Annotations By Experts’~\cite{spinde_plank_krieger_ruas_gipp_aizawa_2021}. Despite the methodology used in the literature toward bias identification, it remains a challenging task due to its nature and lack of universal bias indicators. The BABE dataset is offered in two versions specified by the subgroups they were annotated:
\begin{enumerate}
  \item SG1: 1700 sentences annotated by eight experts.
  \item SG2: 3700 sentences annotated by five experts.
\end{enumerate}
The features provided in original dataset are as follows: 
\begin{itemize}
    \item \textbf{text}: The actual text of the sentence.
    \item \textbf{news link}: The link to the original news article from which the sentence was extracted.
    \item \textbf{outlet}: The media outlet that published the news article.
    \item \textbf{topic}: The topic of the news article.
    \item \textbf{type}: The type of bias (if any) present in the sentence.
    \item \textbf{label bias}: whether the sentence is biased or not.
    \item \textbf{label opinion}: The type of opinion expressed in the sentence, if any.
    \item \textbf{biased words}: The words in the sentence that show bias in python style list.    
\end{itemize}
The distribution of bias in both SG1 and SG2 datasets can be seen in figure 1. 
\begin{figure}[t]
\centering
\includegraphics[width=0.5\textwidth]{SG_lb_bias.png}
\caption{Distribution of Bias across datasets}
\label{fig:my_label}
\end{figure}
Both dataset appear to have similar amount of labels belonging to both classes.
The code for drawing the plots is available in the \text{'Datasetanalysis.ipynb'} in repository.
Additionally the count of label bias votes for each experts is given in figure 2.
\begin{figure}[h]
\centering
\includegraphics[width=0.5\textwidth]{SG_lb_bias.png}
\caption{Individuals label bias tagging for SG1 and SG2 subgroups}
\label{fig:my_label}
\end{figure}
In addition to these datesets, this project also contains scripts for extracting full textual data from some news outlets.\\
\\
\textbf{Notice}: The data extracted for this project is strictly used for academic purposes. It is used solely for the purpose of developing and evaluating machine learning models for media bias classification. No personal data is collected or used, and all data is handled in accordance with ethical guidelines and privacy standards.
\subsection{Models}
In this project I employ a variety of models as a means of investigation for the main model. comparising of three baseline models and a Large Language Model to perform text sequence classificaion. In the result section the models are compared according to the Accuracy, Precision, Recall, and F1 scores.
The Baseline models used here include:
\begin{itemize}
    \item \textbf{Majority Class classifier}: This is a simple classifier that always predicts the most frequent label in the training set. It does not learn any information from the input features and in litrature it is often used a baseline to compare with other (real) classifiers. It’s useful to provide a sanity check and to compare performance against the complex model.
    \item \textbf{Random Guesser}: This classifier generates predictions uniformly at random. The input features are not learned in this model as well. According to the dataset used in this project, using random predictions improve the results since the distribution of 'Biased' and 'Non-Biasd' are similar in this case. 
    \item \textbf{LogisticRegression}: Logistic Regression is a statistical model that uses logistic function to model binary variables. published the news article. This method calculates the probability of belonging to a class by learning from input. As a linear model, it is an effective solution to provide a baseline prediction of classes in the model.
\end{itemize}
The main methodology in this project follows the implementation as in ~\cite{spinde_plank_krieger_ruas_gipp_aizawa_2021}. As the classifier RoBERTa~\cite{liu_ott_goyal_du_joshi_chen_levy_lewis_zettlemoyer_stoyanov_2019} was implemented. RoBERTa is a variant of BERT which was trained on more data and for a longer amount of time. This model outperforms BERT and other state-of-the-art models on a variety of natural language processing tasks~\cite{overview_of_roberta model_2020}. The model was trained and evaluated on a Google Colab environment. The specific hardware used in this project includes a V100 VRAM 16GB GPU and The default CPU, an Intel Xeon CPU with 2 vCPUs (virtual CPUs).
\subsection{Evaluation}
The evaluation of the model is a crucial aspect of this project, essentially providing a measure to show goodness of the model performance in bias identification task. The evaluation is divided into two subsections: 1- Traditional Evaluation Metrics 2- Interpretive Model Evaluation.

\subsubsection{Traditional Evaluation Metrics}
In the first steps the performance of models were tested using the most commonly used metrics. The metrics provide a comprehensive overview of performance while also considering both classes:
\begin{itemize}
    \item \textbf{Accuracy}: It is the ratio of correctly predicted observations to the total observations. It provides an intuitive measure of the overall correctness of the model:
    $$
    \text{Accuracy} = \frac{TP+TN}{TP+TN+FP+FN}
    $$
    \item \textbf{Precision}: This is the ratio of correctly predicted positive observations to the total predicted positive observations:
    $$
    \text{Precision} = \frac{TP}{TP+FP}
    $$
    \item \textbf{Recall}: Recall, or Sensitivity, is the ratio of correctly predicted positive observations to all observations in the actual class. It provides a measure of the model’s ability to find all the positive samples:
    $$
    \text{Recall} = \frac{TP}{TP+FN}
    $$
    \item \textbf{F1 Score}: It is the weighted average of Precision and Recall. It tries to find the balance between precision and recall and is particularly useful when dealing with imbalanced classes(The Classes in my dataset is mostly balanced):
    $$
    \text{F1} = \frac{2 \cdot \text{Precision} \cdot \text{Recall}}{\text{Precision} + \text{Recall}}
    $$
\end{itemize}
\subsubsection{Interpretative Model Evaluation}
In addition to the traditional metrics, a creative evaluation alternative is employed to provide a deeper understanding of the model’s performance. This alternative involves the use of the Anchors method for model interpretation in two approaches.
Essentially, The Anchors method is a technique that can explain individual predictions of black-box classification by discovering a rule that sufficiently “anchors” the prediction locally – such that changes to the rest of the feature values of the instance do not matter~\cite{ribeiro_singh_guestrin_2018}.
\paragraph{Strategy 1: Interpretation of Model Predictions on the Dataset}
The first strategy involves running the Anchors method on the predictions made by the model on the dataset. The Anchors method identifies the words or phrases (the “anchors”) that the model relies on most heavily to make its predictions. These anchors can provide insight into what the model has learned and how it’s making its decisions.
If certain words consistently serve as anchors for ‘biased’ predictions, it suggests that the model has learned to associate these words with media bias. On the other hand, if the anchors seem unrelated to the predicted class, it could indicate that the model is picking up on spurious correlations. The label bias in the dataset is assumed correct and a gold standard for assessing this task.
\paragraph{Strategy 2: Interpretation of Model Predictions on Extracted News Articles}
The second strategy involves extracting some news articles from the news articles in the original data, some using web scraping and some manually. The Anchors method is then run with the model’s predictions on these texts. 

This strategy allows for a more detailed analysis of the model’s decision-making process. By applying the Anchors method to individual sentences or sections within the articles, you can see which parts of the text the model is focusing on to make its predictions.
If the anchors identified in these new articles are similar to those found in the original dataset, it suggests that the model is applying what it has learned to new data. Conversely, if the anchors are very different, it could indicate that the model is struggling to generalize.
\section{Results}
This section presents the results of the fine-tuning process applied to the RoBERTa language model for the task of media bias classification.
\subsection{Model Fine-tuning}
The RoBERTa model was fine-tuned using a stratified 5-fold cross-validation approach. This method ensures that each fold of the dataset contains an equal proportion of each targeted class, providing a robust estimate of the model’s performance.
\subsection{Handling Class Imbalance}
The two dataset used in this project did not exhibit class imbalance, however during the process of cross-validation It was noted(please refer to figure 3) some classes were under-represented in the data. This could lead to a model that performs well on the majority class but poorly on the minority class.

\begin{figure}[h]
\centering
\includegraphics[width=0.5\textwidth]{fail_cm_1.png}
\caption{failure demonstrated by confusion matrix within two selected folds}
\label{fig:my_label}
\end{figure}
To address this issue, an oversampling method was implemented within each fold during the training process. Oversampling involves randomly duplicating examples from the minority class in the training data to balance the class distribution. This ensures that the model is exposed to enough examples of each class during training, improving its ability to generalize to under-represented classes.

Through the combination of stratified 5-fold cross-validation and oversampling, the fine-tuned RoBERTa model was able to learn from a balanced representation of each class, leading to more robust and reliable performance in the media bias classification task.
\subsection{Traditional Evaluation Metrics}
Considering the difference in the number of sentences within each dataset, they are analyzed separately, here is a brief summary of results from SG1 dataset:
\begin{itemize}
    \item \textbf{Majority Class classifier}: It always predicts class 0. That’s why the recall for class 0 is 1.00 (it correctly identifies all instances of class 0), but the recall for class 1 is 0.00 (it fails to identify any instances of class 1). The overall accuracy of 0.54 indicates that 54% of SG1 data belong to class 0.
    \item \textbf{Random Guesser}:  The precision, recall, and F1-score are roughly equal for both classes, indicating that it’s equally likely to guess either class. The overall accuracy of 0.48 is close to 0.5, as you’d expect from random guessing. 
    \item \textbf{LogisticRegression}: This model has higher precision, recall, and F1-score for both classes compared to the other two classifiers, indicating that it is doing a better job of identifying both classes. The overall accuracy of 0.66 means it is correct about 66% of the time.
\end{itemize}
In these numbers macro avg was selected as the default averaging scheme for the metrics(the full result is present in {'finetuning.ipynb'}). Please note that the results of these algorithm does not necessarily indicate the distribution of labels in the corresponding dataset, this is mainly due o randomised train/test split before applying the models.

\begin{figure}
    \centering
    \includegraphics[width=0.5\linewidth]{cm_SG1_random_guess.png}
    \caption{confusion matrix belonging to the random guesses SG1[value 1 indicate bias]}
    \label{fig:enter-label}
\end{figure}
The metrics from two datasets show a consistent pattern. Additionally, according to logistic regression results it can be observed that the increase in the number of data in each group has a substantial effect on learning from data.
On the other hand does not show a promising result for both SG1 and SG2 datasets. Regarding SG1 dataset, the model exhibit accuracy rate of 0.46 which is slightly worse than random guessing, similarly a recall of 0.42 suggests that the model identifies only 42\% of all True positive instances. Optimistically a cross-entropy loss of 0.54 suggest that there is still room for improvement.
In this context we need to improve rate of correctly predicted bias labels, therefore we have maximize accuracy and precision to enhance the overall correctness and lower the false positive rate.

\begin{table}[b]
\caption{Baselines macro avg results across datasets}
\begin{tabular}{llllll}
{\color[HTML]{000000} Model name} & {\color[HTML]{000000} Accuracy} & {\color[HTML]{000000} Precision} & {\color[HTML]{000000} Recall} & F1   & Dataset \\
Majority Class                    & 0.54                            & 0.27                             & 0.50                          & 0.35 & SG1     \\
Random Guesser                    & 0.48                            & 0.48                             & 0.48                          & 0.48 & SG1     \\
Logistic Regression               & 0.66                            & 0.66                             & 0.66                          & 0.66 & SG1     \\
Majority Class                    & 0.51                            & 0.26                             & 0.50                          & 0.34 & SG2     \\
Random Guesser                    & 0.50                            & 0.50                             & 0.50                          & 0.50 & SG2     \\
Logistic Regression               & 0.74                            & 0.74                             & 0.74                          & 0.74 & SG2    
\end{tabular}
\end{table}
\begin{table}[b]
\caption{language model performance metrics}
\begin{tabular}{cccccccc}
CV Loss & \multicolumn{1}{l}{CV Accuracy} & \multicolumn{1}{l}{CV Precision} & \multicolumn{1}{l}{CV Recall} & \multicolumn{1}{r}{CV F1 Score} & \multicolumn{1}{l}{CV Micro F1} & \multicolumn{1}{l}{CV Weighted F1} & \multicolumn{1}{l}{Dataset} \\
0.67    & 0.52                            & 0.50                             & 0.50                          & 0.43                            & 0.52                            & 0.43                               & SG1                         \\
0.54    & 0.46                            & 0.54                             & 0.42                          & 0.44                            & 0.46                            & 0.44                               & SG2                        
\end{tabular}
\end{table}
\subsection{Interpretative Model Evaluation}

\section{Conclusion and Discussion}
\bibliography{anthology,acl2020}
\bibliographystyle{acl_natbib}
\end{document}
