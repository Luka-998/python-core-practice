# Metric tracker tracks the name of ML model and it's metric parameters

# model_name -> <str> "LogisticRegression"
# metrics -> <dict> "f1","recall","accuracy"..
from sklearn.linear_model import LogisticRegression,LinearRegression

model1 = LogisticRegression()
metrics1 = {'f1':0.8,'recall':0.65,'accuracy':0.9,'roc_auc_score':0.32}

model2 = LinearRegression()
metrics2 = {'r2':0.88,'R':0.54}

model3 = LogisticRegression()
metrics3 = {'f1':0.86,'recall':0.92,'accuracy':0.95,'roc_auc_score':0.88}

class MetricTracker:
    def __init__(self,model,metrics):
        self.model= model
        self.metrics = metrics
    def __repr__(self):
        return (
            f"Model name: {self.model.__class__.__name__}"
            f"Model metrics: {self.metrics!r}"
        )
    def __contains__(self, item):
        return item in self.metrics
    
    def __add__(self,other):
        
        """
        Addition is allowed only if models are the same!

        """
        if self.model.__class__.__name__ == other.model.__class__.__name__:
            avg_metrics = {}
            for metric,value in self.metrics.items():
                mt1 = value
                mt2 = other.metrics[metric]
                avg_metrics[metric] = (mt1+mt2)/2
            #for metric,value in self.metrics.items():
                #for metric2,value2 in other.metrics.items():
                    #if metric == metric2:
                        #avg_metrics[metric] = (value+value2)/ 2
            obj = MetricTracker(self.model,avg_metrics)
            return obj
        else:
            raise ValueError("Can only add metrics from the same model.")

    
run1 = MetricTracker(model1,metrics1)
run2 = MetricTracker(model2,metrics2)
run3 = MetricTracker(model3,metrics3)
res_avg = run1 + run3
print(repr(res_avg))


