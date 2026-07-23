class ExperimentResult:
    def __init__(self,model_name,metrics):
        self.name = model_name
        self.metrics = metrics 
    def __repr__(self):
        return f"Class name: {self.__class__.__name__}, Model name: {self.name}, metrics: {self.metrics}"   
    def __str__(self):
        return f"Metrics: {self.metrics}\nModel: {self.name}"
        
    def __eq__(self,other):
        """ 
            Comparison of the model name!
        
        """
        if not isinstance(other,ExperimentResult):
            return NotImplemented
        return (
            self.name == other.name and self.metrics==other.metrics

        )
    def __add__(self,other):
        if isinstance(other,self.__class__):
            if other.name != self.name:
                raise ValueError("Not the same model!")
            if other.metrics.keys()!=self.metrics.keys():
                raise ValueError("Not the same metrics!")
            else:
                # make average metrics
                new_metrics = {}
                for k,v in other.metrics.items():
                    new_metrics[k] = (self.metrics[k] + v)/2
                result = ExperimentResult(self.name,new_metrics)
                return result
        else:
                return NotImplemented
         
if __name__ == '__main__':
    exp1 = ExperimentResult('DT',{'accuracy':0.96,'recall':0.33})
    exp2 = ExperimentResult('RandomForest',{'accuracy':0.62,'recall':0.73})
    exp3 = ExperimentResult('DT',{'accuracy':0.86,'recall':0.43})
    e = exp1 + exp3
    print(e==exp1)
    print(e==exp3)
    print(id(exp1),id(exp3),id(e))
    print(exp1==exp2)
