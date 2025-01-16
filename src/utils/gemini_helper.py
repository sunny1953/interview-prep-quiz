from .gemini_config import get_gemini_model
from ..models.question import Question

class GeminiHelper:
    def __init__(self):
        self.model = get_gemini_model()
        self.domain_subjects = {
            'Machine Learning': {
                'subjects': ['Deep Learning', 'Natural Language Processing', 'Computer Vision', 'Reinforcement Learning', 'ML Engineering'],
                'topics': {
                    'Deep Learning': ['Neural Networks', 'CNN', 'RNN', 'Transformers', 'GANs'],
                    'Natural Language Processing': ['Text Processing', 'Word Embeddings', 'Language Models', 'Sentiment Analysis', 'Machine Translation'],
                    'Computer Vision': ['Image Processing', 'Object Detection', 'Segmentation', 'Face Recognition', 'Video Analysis'],
                    'Reinforcement Learning': ['Q-Learning', 'Policy Gradients', 'Deep RL', 'Multi-Agent Systems', 'RL Applications'],
                    'ML Engineering': ['Model Deployment', 'MLOps', 'Model Optimization', 'Pipeline Design', 'Model Monitoring']
                }
            },
            'System Design': {
                'subjects': ['System Architecture', 'Distributed Systems', 'Database Design', 'Network Design', 'Cloud Architecture'],
                'topics': {
                    'System Architecture': ['Microservices', 'Monoliths', 'Event-Driven', 'SOA', 'Serverless'],
                    'Distributed Systems': ['Consensus', 'Replication', 'Sharding', 'CAP Theorem', 'Fault Tolerance'],
                    'Database Design': ['SQL vs NoSQL', 'Data Modeling', 'Indexing', 'Partitioning', 'Transactions'],
                    'Network Design': ['Load Balancing', 'CDN', 'API Gateway', 'Service Mesh', 'Network Protocols'],
                    'Cloud Architecture': ['AWS', 'Azure', 'GCP', 'Multi-Cloud', 'Cloud Native']
                }
            },
            'DevOps': {
                'subjects': ['CI/CD', 'Infrastructure', 'Monitoring', 'Security', 'Automation'],
                'topics': {
                    'CI/CD': ['Pipeline Design', 'Version Control', 'Testing', 'Deployment Strategies', 'Release Management'],
                    'Infrastructure': ['IaC', 'Containers', 'Kubernetes', 'Service Mesh', 'Cloud Services'],
                    'Monitoring': ['Logging', 'Metrics', 'Tracing', 'Alerting', 'Performance Monitoring'],
                    'Security': ['DevSecOps', 'Compliance', 'Secret Management', 'Security Scanning', 'Access Control'],
                    'Automation': ['Configuration Management', 'Scripting', 'Task Automation', 'Infrastructure Automation', 'Testing Automation']
                }
            },
            'Cloud Computing': {
                'subjects': ['Cloud Services', 'Cloud Security', 'Cloud Architecture', 'Cloud Native', 'Multi-Cloud'],
                'topics': {
                    'Cloud Services': ['Compute', 'Storage', 'Networking', 'Databases', 'Serverless'],
                    'Cloud Security': ['Identity Management', 'Network Security', 'Data Protection', 'Compliance', 'Security Controls'],
                    'Cloud Architecture': ['Well-Architected Framework', 'High Availability', 'Disaster Recovery', 'Cost Optimization', 'Performance'],
                    'Cloud Native': ['Containers', 'Microservices', 'Service Mesh', 'Kubernetes', 'Cloud Native Patterns'],
                    'Multi-Cloud': ['Strategy', 'Management', 'Integration', 'Migration', 'Hybrid Cloud']
                }
            },
            'English Communication': {
                'subjects': ['Grammar', 'Business Communication', 'Writing Skills', 'Public Speaking', 'Vocabulary'],
                'topics': {
                    'Grammar': ['Verb Tenses', 'Subject-Verb Agreement', 'Articles and Determiners', 'Prepositions', 'Sentence Structure'],
                    'Business Communication': ['Email Writing', 'Report Writing', 'Presentation Skills', 'Meeting Etiquette', 'Professional Tone'],
                    'Writing Skills': ['Essay Writing', 'Technical Writing', 'Creative Writing', 'Proofreading', 'Style Guide'],
                    'Public Speaking': ['Speech Structure', 'Body Language', 'Voice Modulation', 'Audience Engagement', 'Impromptu Speaking'],
                    'Vocabulary': ['Business Terms', 'Idioms', 'Phrasal Verbs', 'Synonyms', 'Antonyms']
                }
            },
            'Augmented Reality': {
                'subjects': ['AR Development', 'Spatial Computing', 'Computer Vision', 'AR UX Design', 'AR Hardware'],
                'topics': {
                    'AR Development': ['ARKit', 'ARCore', 'Vuforia', 'WebXR', 'SLAM'],
                    'Spatial Computing': ['6DOF Tracking', 'Spatial Mapping', 'Anchor Points', 'World Tracking', 'Plane Detection'],
                    'Computer Vision': ['Image Recognition', 'Feature Detection', 'Marker Tracking', 'Object Detection', 'Scene Understanding'],
                    'AR UX Design': ['Spatial UI', 'Gesture Recognition', 'Environmental Awareness', 'User Interaction', 'Visual Feedback'],
                    'AR Hardware': ['HoloLens', 'Magic Leap', 'Mobile AR', 'Smart Glasses', 'Depth Sensors']
                }
            },
            'Virtual Reality': {
                'subjects': ['VR Development', 'VR Interaction', 'VR Graphics', 'VR Audio', 'VR Performance'],
                'topics': {
                    'VR Development': ['OpenXR', 'SteamVR', 'Oculus SDK', 'WebVR', 'Unity XR'],
                    'VR Interaction': ['Controllers', 'Hand Tracking', 'Locomotion', 'Physics', 'Haptics'],
                    'VR Graphics': ['Rendering', 'Optimization', 'Shaders', 'Post-processing', 'VR UI'],
                    'VR Audio': ['Spatial Audio', '3D Sound', 'HRTF', 'Audio Occlusion', 'Reverb Zones'],
                    'VR Performance': ['Frame Rate', 'Latency', 'Optimization', 'Foveated Rendering', 'Multi-pass Rendering']
                }
            },
            '3D Modeling': {
                'subjects': ['Modeling Techniques', 'Texturing', 'Rigging', 'Animation', 'Rendering'],
                'topics': {
                    'Modeling Techniques': ['Polygon Modeling', 'Sculpting', 'Hard Surface', 'Organic Modeling', 'Topology'],
                    'Texturing': ['UV Mapping', 'PBR Materials', 'Substance Painter', 'Normal Maps', 'Texture Baking'],
                    'Rigging': ['Skeletal Rigging', 'Weight Painting', 'IK/FK', 'Facial Rigging', 'Deformers'],
                    'Animation': ['Keyframe Animation', 'Motion Capture', 'Procedural Animation', 'Blend Shapes', 'Animation Curves'],
                    'Rendering': ['Lighting', 'Materials', 'Ray Tracing', 'Global Illumination', 'Compositing']
                }
            },
            'Unity Development': {
                'subjects': ['Unity Core', 'Graphics & Rendering', 'Game Systems', 'Unity Physics', 'Unity Scripting'],
                'topics': {
                    'Unity Core': ['Component System', 'Scene Management', 'Asset Pipeline', 'Unity Services', 'Build Settings'],
                    'Graphics & Rendering': ['Universal RP', 'HDRP', 'Shader Graph', 'VFX Graph', 'Post Processing'],
                    'Game Systems': ['Input System', 'Animation System', 'UI Toolkit', 'Networking', 'Audio System'],
                    'Unity Physics': ['Rigidbody Physics', 'Colliders', 'Raycasting', 'Physics Materials', 'Joints'],
                    'Unity Scripting': ['MonoBehaviour', 'Coroutines', 'Events', 'Scriptable Objects', 'DOTS']
                }
            },
            'Unreal Engine': {
                'subjects': ['Blueprints', 'Unreal Graphics', 'Game Framework', 'Unreal Physics', 'Unreal C++'],
                'topics': {
                    'Blueprints': ['Visual Scripting', 'Blueprint Communication', 'Blueprint Interface', 'Event Graph', 'Construction Script'],
                    'Unreal Graphics': ['Material Editor', 'Post Process', 'Niagara VFX', 'Lighting', 'Lumen'],
                    'Game Framework': ['Game Mode', 'Pawn System', 'Level Blueprint', 'Gameplay Framework', 'Replication'],
                    'Unreal Physics': ['PhysX', 'Chaos Physics', 'Physical Animation', 'Constraints', 'Vehicle System'],
                    'Unreal C++': ['UObject System', 'Garbage Collection', 'Reflection System', 'Smart Pointers', 'Gameplay Classes']
                }
            },
            'Blender': {
                'subjects': ['Modeling Tools', 'Animation System', 'Materials & Nodes', 'Simulation', 'Scripting'],
                'topics': {
                    'Modeling Tools': ['Edit Mode Tools', 'Modifiers', 'Geometry Nodes', 'Sculpting', 'Retopology'],
                    'Animation System': ['Armature', 'Action Editor', 'NLA Editor', 'Constraints', 'Drivers'],
                    'Materials & Nodes': ['Shader Editor', 'Texture Nodes', 'Compositing', 'Material Preview', 'EEVEE vs Cycles'],
                    'Simulation': ['Particle Systems', 'Cloth Physics', 'Fluid Simulation', 'Rigid Body', 'Soft Body'],
                    'Scripting': ['Python API', 'Add-ons', 'Automation', 'Custom Tools', 'UI Development']
                }
            },
            'Autodesk Maya': {
                'subjects': ['Modeling Workflow', 'Animation Tools', 'Dynamics', 'Rendering', 'MEL Scripting'],
                'topics': {
                    'Modeling Workflow': ['NURBS', 'Polygon Tools', 'UV Editor', 'Deformers', 'XGen'],
                    'Animation Tools': ['Graph Editor', 'Time Editor', 'Character Controls', 'Motion Paths', 'Animation Layers'],
                    'Dynamics': ['nCloth', 'nParticles', 'nHair', 'Bullet Physics', 'Fields'],
                    'Rendering': ['Arnold', 'Maya Hardware 2.0', 'Render Layers', 'Light Types', 'Render Settings'],
                    'MEL Scripting': ['MEL Commands', 'Custom Tools', 'UI Creation', 'Automation', 'Pipeline Integration']
                }
            },
            'Cybersecurity': {
                'subjects': ['Network Security', 'Application Security', 'Security Operations', 'Cryptography', 'Identity & Access Management'],
                'topics': {
                    'Network Security': ['Firewalls', 'IDS/IPS', 'VPN', 'Network Protocols', 'Zero Trust'],
                    'Application Security': ['OWASP Top 10', 'Secure Coding', 'Vulnerability Assessment', 'Penetration Testing', 'API Security'],
                    'Security Operations': ['Incident Response', 'Threat Hunting', 'SIEM', 'Security Monitoring', 'Malware Analysis'],
                    'Cryptography': ['Encryption', 'Digital Signatures', 'PKI', 'Hash Functions', 'Key Management'],
                    'Identity & Access Management': ['Authentication', 'Authorization', 'SSO', 'MFA', 'Privileged Access']
                }
            },
            'Software Development': {
                'subjects': ['Backend Development', 'Frontend Development', 'System Design', 'DevOps', 'Software Architecture'],
                'topics': {
                    'Backend Development': ['API Design', 'Database Design', 'Caching', 'Microservices', 'Message Queues'],
                    'Frontend Development': ['React', 'State Management', 'Performance Optimization', 'Responsive Design', 'Web Security'],
                    'System Design': ['Scalability', 'High Availability', 'Load Balancing', 'Distributed Systems', 'Data Storage'],
                    'DevOps': ['CI/CD', 'Containerization', 'Infrastructure as Code', 'Monitoring', 'Cloud Services'],
                    'Software Architecture': ['Design Patterns', 'SOLID Principles', 'Clean Architecture', 'Event-Driven', 'Domain-Driven Design']
                }
            },
            'Data Science': {
                'subjects': ['Machine Learning', 'Statistics', 'Data Engineering', 'Deep Learning', 'MLOps'],
                'topics': {
                    'Machine Learning': ['Supervised Learning', 'Unsupervised Learning', 'Model Evaluation', 'Feature Engineering', 'Ensemble Methods'],
                    'Statistics': ['Probability', 'Hypothesis Testing', 'Regression Analysis', 'Experimental Design', 'Bayesian Statistics'],
                    'Data Engineering': ['ETL', 'Data Warehousing', 'Big Data', 'Data Pipelines', 'Data Quality'],
                    'Deep Learning': ['Neural Networks', 'CNN', 'RNN', 'Transformers', 'Transfer Learning'],
                    'MLOps': ['Model Deployment', 'Model Monitoring', 'Version Control', 'Pipeline Automation', 'Model Serving']
                }
            }
        }
        self.current_domain = None
        self.subjects = []
        self.topics = {}

    def set_domain_subjects(self, domain):
        """Set the subjects and topics based on selected domain"""
        print(f"Setting domain subjects for: {domain}")
        if domain in self.domain_subjects:
            self.current_domain = domain
            domain_data = self.domain_subjects[domain]
            self.subjects = domain_data['subjects']
            self.topics = domain_data['topics']
            print(f"Successfully set domain. Subjects: {self.subjects}")
            print(f"Available topics: {self.topics}")
        else:
            print(f"Error: Domain {domain} not found in available domains: {list(self.domain_subjects.keys())}")
            raise ValueError(f"Domain {domain} not supported. Please select from: {list(self.domain_subjects.keys())}")

    def _validate_grammar_answer(self, question_text, options, correct_answer, topic):
        """Validate grammar question answers"""
        prompt = f"""As an expert English Grammar instructor, verify if this answer is correct:

Question: "{question_text}"
Options: {options}
Given Answer: "{correct_answer}"
Topic: {topic}

Requirements:
1. Verify if the given answer follows standard English grammar rules
2. Check if it's actually the best option among the choices
3. Ensure it matches the specific grammar rule being tested
4. Confirm there are no exceptions or special cases that would make another option correct

Respond with ONLY "VALID" if the answer is correct, or "INVALID: reason" if incorrect."""

        response = self.model.generate_content(prompt)
        validation = response.text.strip()
        print(f"Grammar validation result: {validation}")
        return validation.startswith("VALID")

    def _validate_communication_answer(self, question_text, options, correct_answer, topic):
        """Validate communication question answers"""
        prompt = f"""As an expert English Communication instructor, verify if this answer is correct:

Question: "{question_text}"
Options: {options}
Given Answer: "{correct_answer}"
Topic: {topic}

Requirements:
1. Verify if the answer follows standard business English practices
2. Check if it's the most appropriate option in a professional context
3. Ensure it matches current business communication best practices
4. Confirm there are no context-specific situations that would make another option better

Respond with ONLY "VALID" if the answer is correct, or "INVALID: reason" if incorrect."""

        response = self.model.generate_content(prompt)
        validation = response.text.strip()
        print(f"Communication validation result: {validation}")
        return validation.startswith("VALID")

    async def generate_question(self, subject, difficulty):
        """Generate a domain-specific question using Gemini"""
        try:
            if not self.current_domain:
                print("Error: No domain selected")
                return None
                
            if not self.subjects:
                print("Error: No subjects available")
                return None
                
            if subject not in self.subjects:
                print(f"Error: Invalid subject '{subject}'. Available subjects: {self.subjects}")
                return None
                
            print(f"Generating question for subject: {subject}, difficulty: {difficulty}")
            topics = self.topics.get(subject, [subject])
            if not topics:
                print(f"Error: No topics found for subject {subject}")
                return None
                
            topic = topics[hash(str(difficulty) + subject) % len(topics)]
            print(f"Selected topic: {topic}")
            
            difficulty_levels = {
                'easy': 'basic understanding and fundamental concepts',
                'medium': 'practical application and intermediate concepts',
                'hard': 'advanced concepts and real-world scenarios'
            }
            
            if difficulty not in difficulty_levels:
                print(f"Error: Invalid difficulty '{difficulty}'. Using 'medium' as default.")
                difficulty = 'medium'

            # Generate the appropriate prompt based on domain and subject
            if self.current_domain == 'English Communication':
                if subject == 'Grammar':
                    prompt = self._get_grammar_prompt(topic, difficulty_levels[difficulty])
                else:
                    prompt = self._get_communication_prompt(subject, topic, difficulty_levels[difficulty])
            else:
                prompt = self._get_technical_prompt(subject, topic, difficulty_levels[difficulty])

            # Make multiple attempts to generate a valid question
            max_attempts = 3
            for attempt in range(max_attempts):
                try:
                    print(f"Attempt {attempt + 1} to generate question")
                    response = self.model.generate_content(prompt)
                    
                    if not response or not response.text:
                        print("Error: Empty response from model")
                        continue
                    
                    text = response.text.strip()
                    print(f"Raw response from model: {text}")
        
        # Parse the response
                    question = self._parse_question_response(text, difficulty)
                    if not question:
                        continue

                    # Validate the answer if it's an English Communication question
                    if self.current_domain == 'English Communication':
                        is_valid = False
                        if subject == 'Grammar':
                            is_valid = self._validate_grammar_answer(
                                question.content, 
                                question.options, 
                                question.correct_answer,
                                question.topic
                            )
                        else:
                            is_valid = self._validate_communication_answer(
                                question.content,
                                question.options,
                                question.correct_answer,
                                question.topic
                            )
                            
                        if not is_valid:
                            print("Answer validation failed, retrying...")
                            continue
                            
                        print("Answer validation passed")
                    
                    return question
                        
                except Exception as e:
                    print(f"Error in attempt {attempt + 1}: {str(e)}")
                    continue
                    
            print(f"Failed to generate valid question after {max_attempts} attempts")
            return None
            
        except Exception as e:
            print(f"Error in generate_question: {str(e)}")
            return None
            
    def _parse_question_response(self, text, difficulty):
        """Parse and validate the question response"""
        try:
            # Split into lines and clean up
            lines = [line.strip() for line in text.split('\n') if line.strip()]
            
            # Find all required components
            components = {
                'QUESTION:': None,
                'OPTIONS:': None,
                'CORRECT:': None,
                'TOPIC:': None
            }
            
            for line in lines:
                for key in components:
                    if line.startswith(key):
                        components[key] = line
                        break
            
            if not all(components.values()):
                print("Error: Missing required components in response")
                print(f"Found components: {components}")
                return None
            
            # Parse question
            question_text = components['QUESTION:'].replace('QUESTION:', '').strip().strip('"').strip("'")
            
            # Parse options
            try:
                options_str = components['OPTIONS:'].replace('OPTIONS:', '').strip()
                options_str = options_str.replace("'", '"')  # Standardize quotes
                import json
                options = json.loads(options_str)
                
                if not isinstance(options, list):
                    print("Error: Options must be a list")
                    return None
                
                if len(options) != 4:
                    print(f"Error: Expected 4 options, got {len(options)}")
                    return None
                    
            except json.JSONDecodeError as e:
                print(f"Error parsing options JSON: {e}")
                print(f"Raw options string: {options_str}")
                return None
            
            # Parse correct answer and topic
            correct_answer = components['CORRECT:'].replace('CORRECT:', '').strip().strip('"').strip("'")
            specific_topic = components['TOPIC:'].replace('TOPIC:', '').strip().strip('"').strip("'")
            
            # Validate all components
            if not all([question_text, options, correct_answer, specific_topic]):
                print("Error: Empty required components")
                return None
            
            if correct_answer not in options:
                print(f"Error: Correct answer '{correct_answer}' not found in options {options}")
                return None
            
            print("Successfully parsed question response")
            return Question(
                content=question_text,
                options=options,
                correct_answer=correct_answer,
                difficulty=difficulty,
                topic=specific_topic
            )
            
        except Exception as e:
            print(f"Error parsing question response: {str(e)}")
            print(f"Raw response: {text}")
            return None
            
    def _get_grammar_prompt(self, topic, difficulty_level):
        """Get the prompt for grammar questions"""
        return f"""You are an expert English Grammar instructor. Generate a multiple-choice question testing knowledge of English grammar rules.

Subject Area: Grammar
Specific Topic: {topic}
Level: {difficulty_level}

Requirements:
1. Question must test specific grammar rules and their application
2. For Verb Tenses: Test proper usage of tenses in context
3. For Subject-Verb Agreement: Test agreement in complex sentences
4. For Articles/Determiners: Test proper article usage
5. For Prepositions: Test correct preposition usage
6. For Sentence Structure: Test proper sentence construction
7. All options must be grammatically plausible but only one correct
8. Include exactly 4 options
9. Make sure the correct answer follows standard English grammar rules

Respond in this EXACT format (including the exact labels and quotes):
QUESTION: "Write your question here"
OPTIONS: ["option1", "option2", "option3", "option4"]
CORRECT: "exact text of correct option"
TOPIC: "{topic}"

Example format (but make your own question):
QUESTION: "Which sentence demonstrates correct subject-verb agreement?"
OPTIONS: ["The team of experts have submitted their report.", "The team of experts has submitted their report.", "The team of experts have submitted its report.", "The team of experts has submitted its reports."]
CORRECT: "The team of experts has submitted their report."
TOPIC: "Subject-Verb Agreement"

Make sure your response follows this exact format with quotes and square brackets."""

    def _get_communication_prompt(self, subject, topic, difficulty_level):
        """Get the prompt for communication questions"""
        return f"""You are an expert English Communication instructor. Generate a practical multiple-choice question for a business English assessment.

Subject Area: {subject}
Specific Topic: {topic}
Level: {difficulty_level}

Requirements:
1. Question must be directly related to professional English communication
2. Focus on real business scenarios and workplace communication
3. For Business Communication: Focus on email, presentation, or meeting scenarios
4. For Writing Skills: Focus on business documents and professional writing
5. For Vocabulary: Use words in proper business context
6. All options must be plausible in a business context
7. Include exactly 4 options
8. Make sure the correct answer follows standard business English practices

Respond in this EXACT format (including the exact labels and quotes):
QUESTION: "Write your question here"
OPTIONS: ["option1", "option2", "option3", "option4"]
CORRECT: "exact text of correct option"
TOPIC: "{topic}"

Example format (but make your own question):
QUESTION: "In a formal business email, which opening line is most appropriate for a client you've never met?"
OPTIONS: ["Hey there!", "Dear Sir/Madam,", "Hi,", "What's up,"]
CORRECT: "Dear Sir/Madam,"
TOPIC: "Email Writing"

Make sure your response follows this exact format with quotes and square brackets."""

    def _get_technical_prompt(self, subject, topic, difficulty_level):
        """Get the prompt for technical questions"""
        return f"""You are an expert {self.current_domain} interviewer. Generate a technical multiple-choice question for an interview.

Subject Area: {subject}
Specific Topic: {topic}
Level: {difficulty_level}

Requirements:
1. Question must be highly technical and specific to {self.current_domain}
2. Focus on practical, real-world scenarios
3. All options must be plausible, but only one correct
4. Include exactly 4 options
5. Make sure the correct answer is included in the options

Respond in this EXACT format (including the exact labels and quotes):
QUESTION: "Write your question here"
OPTIONS: ["option1", "option2", "option3", "option4"]
CORRECT: "exact text of correct option"
TOPIC: "{topic}"

Example format (but make your own question):
QUESTION: "What is the primary purpose of a Web Application Firewall (WAF) in application security?"
OPTIONS: ["Monitor network traffic", "Filter malicious HTTP requests", "Encrypt database connections", "Manage user sessions"]
CORRECT: "Filter malicious HTTP requests"
TOPIC: "Application Security"

Make sure your response follows this exact format with quotes and square brackets."""

    async def generate_hint(self, question, topic):
        """Generate a domain-specific hint"""
        prompt = f"""As an expert {self.current_domain} interviewer, provide a strategic hint for this technical question:

Question: "{question}"
Topic: {topic}

Your hint should:
1. Guide the candidate's thinking process
2. Highlight a key technical concept without revealing the answer
3. Be specific to {self.current_domain} best practices
4. Help demonstrate deep technical understanding

Keep the hint concise and technically precise."""
        
        response = self.model.generate_content(prompt)
        return response.text.strip()

    async def explain_answer(self, question, correct_answer, topic):
        """Generate a concise explanation"""
        prompt = f"""As an expert {self.current_domain} interviewer, explain this technical question in a single, clear paragraph:

Question: "{question}"
Correct Answer: {correct_answer}
Topic: {topic}

Provide a concise explanation that covers:
1. Why this is the correct answer
2. Key technical points
3. Common mistakes to avoid

Keep it brief and focused. Use `backticks` for technical terms."""
        
        response = self.model.generate_content(prompt)
        return response.text.strip() 