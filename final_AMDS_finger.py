# -*- coding: mbcs -*-
from part import *
from material import *
from section import *
from assembly import *
from step import *
from interaction import *
from load import *
from mesh import *
from optimization import *
from job import *
from sketch import *
from visualization import *
from connectorBehavior import *
#import Vara_ronn

#Load variables
#exec(open("C:\Users\ronn\OneDrive\Desktop\AMDS\Vara_ronn").read())
#f=open("C:\\Users\\ronn\\OneDrive\\Desktop\\AMDS\\Vara_ronn.py")
#print(f.read())
#state1 = 50.0
#state2 = 20.0
#state3 = 10.0
#state4 = 2.0

exec(open("C:\\temp\\Vara_ronn.py").read())

La = state1
H = state2
Lc = state3
T = state4
Hc = 5
Lk = (La- 3*Lc)/2

pressure = pressure1
#force = 0.8621

s1 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', 
        sheetSize=200.0)
    
g, v, d, c = s1.geometry, s1.vertices, s1.dimensions, s1.constraints

s1.setPrimaryObject(option=STANDALONE)

    
#Changeable code
# outer sketch ------------------------------------------------------
s1.Line(point1=(0.0, 0.0), point2=(La, 0.0))
s1.HorizontalConstraint(entity=g[2], addUndoState=False)
# s.ObliqueDimension(vertex1=v[0], vertex2=v[1], textPoint=(-21.2945175170898,
#    -20.1835823059082), value=state1)
s1.Line(point1=(0.0, 0.0), point2=(0.0, H))
s1.VerticalConstraint(entity=g[3], addUndoState=False)
s1.PerpendicularConstraint(entity1=g[2], entity2=g[3], addUndoState=False)
s1.Line(point1=(0.0, H), point2=(Lc, H))
s1.HorizontalConstraint(entity=g[4], addUndoState=False)
s1.PerpendicularConstraint(entity1=g[3], entity2=g[4], addUndoState=False)
s1.Line(point1=(Lc, H), point2=(Lc, Hc))
s1.VerticalConstraint(entity=g[5], addUndoState=False)
s1.PerpendicularConstraint(entity1=g[4], entity2=g[5], addUndoState=False)
s1.Line(point1=(Lc, Hc), point2=(Lc + Lk, Hc))
s1.HorizontalConstraint(entity=g[6], addUndoState=False)
s1.PerpendicularConstraint(entity1=g[5], entity2=g[6], addUndoState=False)
s1.Line(point1=(Lc + Lk, Hc), point2=(Lc + Lk, H))
s1.VerticalConstraint(entity=g[7], addUndoState=False)
s1.PerpendicularConstraint(entity1=g[6], entity2=g[7], addUndoState=False)
s1.Line(point1=(Lc + Lk, H), point2=(2 * Lc + Lk, H))
s1.HorizontalConstraint(entity=g[8], addUndoState=False)
s1.PerpendicularConstraint(entity1=g[7], entity2=g[8], addUndoState=False)
s1.Line(point1=(2 * Lc + Lk, H), point2=(2 * Lc + Lk, Hc))
s1.VerticalConstraint(entity=g[9], addUndoState=False)
s1.PerpendicularConstraint(entity1=g[8], entity2=g[9], addUndoState=False)
s1.Line(point1=(2 * Lc + Lk, Hc), point2=(2 * Lc + 2 * Lk, Hc))
s1.HorizontalConstraint(entity=g[10], addUndoState=False)
s1.PerpendicularConstraint(entity1=g[9], entity2=g[10], addUndoState=False)
s1.Line(point1=(2 * Lc + 2 * Lk, Hc), point2=(2 * Lc + 2 * Lk, H))
s1.VerticalConstraint(entity=g[11], addUndoState=False)
s1.PerpendicularConstraint(entity1=g[10], entity2=g[11], addUndoState=False)
s1.Line(point1=(2 * Lc + 2 * Lk, H), point2=(La, H))
s1.HorizontalConstraint(entity=g[12], addUndoState=False)
s1.PerpendicularConstraint(entity1=g[11], entity2=g[12], addUndoState=False)
s1.Line(point1=(La, H), point2=(La, 0))
s1.VerticalConstraint(entity=g[13], addUndoState=False)
s1.PerpendicularConstraint(entity1=g[12], entity2=g[13], addUndoState=False)
# s.ObliqueDimension(vertex1=v[0], vertex2=v[2], textPoint=(-41.9849395751953,
#   0.226783752441406), value=state2)
# s.ObliqueDimension(vertex1=v[11], vertex2=v[1], textPoint=(29.4498672485352,
#    -2.64579010009766), value=state2)
p = mdb.models['Model-1'].Part(name='Part-1', dimensionality=THREE_D,
                               type=DEFORMABLE_BODY)
p = mdb.models['Model-1'].parts['Part-1']
p.BaseSolidExtrude(sketch=s1, depth=20.0)
s1.unsetPrimaryObject()
p = mdb.models['Model-1'].parts['Part-1']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
del mdb.models['Model-1'].sketches['__profile__']
p = mdb.models['Model-1'].parts['Part-1']
p.DatumPlaneByPrincipalPlane(principalPlane=XYPLANE, offset=4.0)
p = mdb.models['Model-1'].parts['Part-1']
e, d1 = p.edges, p.datums
t = p.MakeSketchTransform(sketchPlane=d1[2], sketchUpEdge=e[30],
                          sketchPlaneSide=SIDE1, sketchOrientation=RIGHT, origin=(0.0, 0.0,
                                                                                  4.0))
s1 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__',
                                             sheetSize=134.82, gridSpacing=3.37, transform=t)
g, v, d, c = s1.geometry, s1.vertices, s1.dimensions, s1.constraints
s1.setPrimaryObject(option=SUPERIMPOSE)
p = mdb.models['Model-1'].parts['Part-1']
p.projectReferencesOntoSketch(sketch=s1, filter=COPLANAR_EDGES)

#-------------------------------------------------------------------------
# inner sketch----------------------------------------------------------
s1.Line(point1=(0.0+T, 0.0+T), point2=(La-T, 0.0+T))
s1.HorizontalConstraint(entity=g[2], addUndoState=False)
# s.ObliqueDimension(vertex1=v[0], vertex2=v[1], textPoint=(-21.2945175170898,
#    -20.1835823059082), value=state1)
s1.Line(point1=(0.0+T, 0.0+T), point2=(0.0+T, H-T))
s1.VerticalConstraint(entity=g[3], addUndoState=False)
s1.PerpendicularConstraint(entity1=g[2], entity2=g[3], addUndoState=False)
s1.Line(point1=(0.0+T, H-T), point2=(Lc-T, H-T))
s1.HorizontalConstraint(entity=g[4], addUndoState=False)
s1.PerpendicularConstraint(entity1=g[3], entity2=g[4], addUndoState=False)
s1.Line(point1=(Lc-T, H-T), point2=(Lc-T, Hc-T))
s1.VerticalConstraint(entity=g[5], addUndoState=False)
s1.PerpendicularConstraint(entity1=g[4], entity2=g[5], addUndoState=False)
s1.Line(point1=(Lc-T, Hc-T), point2=(Lc + Lk+T, Hc-T))
s1.HorizontalConstraint(entity=g[6], addUndoState=False)
s1.PerpendicularConstraint(entity1=g[5], entity2=g[6], addUndoState=False)
s1.Line(point1=(Lc + Lk+T, Hc-T), point2=(Lc + Lk+T, H-T))
s1.VerticalConstraint(entity=g[7], addUndoState=False)
s1.PerpendicularConstraint(entity1=g[6], entity2=g[7], addUndoState=False)
s1.Line(point1=(Lc + Lk+T, H-T), point2=(2 * Lc + Lk-T, H-T))
s1.HorizontalConstraint(entity=g[8], addUndoState=False)
s1.PerpendicularConstraint(entity1=g[7], entity2=g[8], addUndoState=False)
s1.Line(point1=(2 * Lc + Lk-T, H-T), point2=(2 * Lc + Lk-T, Hc-T))
s1.VerticalConstraint(entity=g[9], addUndoState=False)
s1.PerpendicularConstraint(entity1=g[8], entity2=g[9], addUndoState=False)
s1.Line(point1=(2 * Lc + Lk-T, Hc-T), point2=(2 * Lc + 2 * Lk+T, Hc-T))
s1.HorizontalConstraint(entity=g[10], addUndoState=False)
s1.PerpendicularConstraint(entity1=g[9], entity2=g[10], addUndoState=False)
s1.Line(point1=(2 * Lc + 2 * Lk+T, Hc-T), point2=(2 * Lc + 2 * Lk+T, H-T))
s1.VerticalConstraint(entity=g[11], addUndoState=False)
s1.PerpendicularConstraint(entity1=g[10], entity2=g[11], addUndoState=False)
s1.Line(point1=(2 * Lc + 2 * Lk+T, H-T), point2=(La-T, H-T))
s1.HorizontalConstraint(entity=g[12], addUndoState=False)
s1.PerpendicularConstraint(entity1=g[11], entity2=g[12], addUndoState=False)
s1.Line(point1=(La-T, H-T), point2=(La-T, 0+T))
s1.VerticalConstraint(entity=g[13], addUndoState=False)
s1.PerpendicularConstraint(entity1=g[12], entity2=g[13], addUndoState=False)
# s1.ObliqueDimension(vertex1=v[0], vertex2=v[1], textPoint=(-19.7394065856934,
#    11.6468391418457), value=state3)
session.viewports['Viewport: 1'].view.setValues(nearPlane=106.1,
                                                farPlane=163.545, width=134.024, height=58.4936, cameraPosition=(
        -15.1913, -4.30403, 144.822), cameraTarget=(-15.1913, -4.30403, 10))
session.viewports['Viewport: 1'].view.setValues(cameraPosition=(-2.94987,
                                                                12.7513, 144.822), cameraTarget=(-2.94987, 12.7513, 10))
session.viewports['Viewport: 1'].view.setValues(nearPlane=111.082,
                                                farPlane=158.563, width=86.9117, height=37.9318, cameraPosition=(
        -6.91756, 14.7611, 144.822), cameraTarget=(-6.91756, 14.7611, 10))
# s1.ObliqueDimension(vertex1=v[4], vertex2=v[5], textPoint=(0.255085468292236,
#    14.8020210266113), value=state3)
# s1.ObliqueDimension(vertex1=v[8], vertex2=v[9], textPoint=(21.7784233093262,
#    15.7851333618164), value=state3)
session.viewports['Viewport: 1'].view.setValues(nearPlane=109.144,
                                                farPlane=160.5, width=99.1674, height=43.2806, cameraPosition=(
        -18.0875, 10.0777, 144.822), cameraTarget=(-18.0875, 10.0777, 10))
# s1.ObliqueDimension(vertex1=v[11], vertex2=v[0], textPoint=(-35.8929290771484,
#    -1.27991199493408), value=state4)
# s1.ObliqueDimension(vertex1=v[9], vertex2=v[10], textPoint=(32.8332366943359,
#    0.309226036071777), value=state4)
session.viewports['Viewport: 1'].view.setValues(nearPlane=102.096,
                                                farPlane=167.548, width=143.748, height=62.7374, cameraPosition=(
        -10.6119, 17.1345, 144.822), cameraTarget=(-10.6119, 17.1345, 10))
session.viewports['Viewport: 1'].view.setValues(cameraPosition=(-7.63412,
                                                                0.603218, 144.822),
                                                cameraTarget=(-7.63412, 0.603218, 10))
session.viewports['Viewport: 1'].view.setValues(nearPlane=109.144,
                                                farPlane=160.5, width=99.1674, height=43.2806, cameraPosition=(
        -9.40268, 3.09716, 144.822), cameraTarget=(-9.40268, 3.09716, 10))
p = mdb.models['Model-1'].parts['Part-1']
e1, d2 = p.edges, p.datums
p.CutExtrude(sketchPlane=d2[2], sketchUpEdge=e1[30], sketchPlaneSide=SIDE1,
             sketchOrientation=RIGHT, sketch=s1, depth=12.0,
             flipExtrudeDirection=ON)
s1.unsetPrimaryObject()          #----------------------------cut extrude
del mdb.models['Model-1'].sketches['__profile__']
mdb.models['Model-1'].Material(name='Material-1')
mdb.models['Model-1'].materials['Material-1'].Density(table=((1.049e-09, ), ))
mdb.models['Model-1'].materials['Material-1'].Hyperelastic(materialType=
    ISOTROPIC, table=((0.11, 0.02, 0.0, 0.0, 0.0, 0.0), ), testData=OFF, type=
    YEOH, volumetricResponse=VOLUMETRIC_DATA)
mdb.models['Model-1'].HomogeneousSolidSection(material='Material-1', name=
    'Section-1', thickness=None)
mdb.models['Model-1'].parts['Part-1'].Set(cells=
    mdb.models['Model-1'].parts['Part-1'].cells.getSequenceFromMask(('[#1 ]', 
    ), ), name='Set-1')
mdb.models['Model-1'].parts['Part-1'].SectionAssignment(offset=0.0, 
    offsetField='', offsetType=MIDDLE_SURFACE, region=
    mdb.models['Model-1'].parts['Part-1'].sets['Set-1'], sectionName=
    'Section-1', thicknessAssignment=FROM_SECTION)
mdb.models['Model-1'].parts['Part-1'].Surface(name='inn', side1Faces=
    mdb.models['Model-1'].parts['Part-1'].faces.getSequenceFromMask((
    '[#fffc000 ]', ), ))
mdb.models['Model-1'].parts['Part-1'].Surface(name='out', side1Faces=
    mdb.models['Model-1'].parts['Part-1'].faces.getSequenceFromMask(('[#aa ]', 
    ), ))
mdb.models['Model-1'].parts['Part-1'].Set(faces=
    mdb.models['Model-1'].parts['Part-1'].faces.getSequenceFromMask(('[#800 ]', 
    ), ), name='fixed')
mdb.models['Model-1'].rootAssembly.DatumCsysByDefault(CARTESIAN)
mdb.models['Model-1'].rootAssembly.Instance(dependent=ON, name='Part-1-1', 
    part=mdb.models['Model-1'].parts['Part-1'])
mdb.models['Model-1'].StaticStep(initialInc=0.001, name='press', nlgeom=ON, 
    previous='Initial')
mdb.models['Model-1'].ContactProperty('IntProp-1')
mdb.models['Model-1'].interactionProperties['IntProp-1'].TangentialBehavior(
    formulation=FRICTIONLESS)
mdb.models['Model-1'].SelfContactStd(createStepName='press', 
    interactionProperty='IntProp-1', name='Int-1', surface=
    mdb.models['Model-1'].rootAssembly.instances['Part-1-1'].surfaces['out'], 
    thickness=ON)
mdb.models['Model-1'].EncastreBC(createStepName='Initial', localCsys=None, 
    name='BC-1', region=
    mdb.models['Model-1'].rootAssembly.instances['Part-1-1'].sets['fixed'])
mdb.models['Model-1'].Pressure(amplitude=UNSET, createStepName='press', 
    distributionType=UNIFORM, field='', magnitude=pressure, name='press', region=
    mdb.models['Model-1'].rootAssembly.instances['Part-1-1'].surfaces['inn'])
mdb.models['Model-1'].parts['Part-1'].setMeshControls(elemShape=TET, regions=
    mdb.models['Model-1'].parts['Part-1'].cells.getSequenceFromMask(('[#1 ]', 
    ), ), technique=FREE)
mdb.models['Model-1'].parts['Part-1'].setElementType(elemTypes=(ElemType(
    elemCode=C3D20R, elemLibrary=STANDARD), ElemType(elemCode=C3D15, 
    elemLibrary=STANDARD), ElemType(elemCode=C3D10, elemLibrary=STANDARD)), 
    regions=(mdb.models['Model-1'].parts['Part-1'].cells.getSequenceFromMask((
    '[#1 ]', ), ), ))
mdb.models['Model-1'].parts['Part-1'].seedPart(deviationFactor=0.1, 
    minSizeFactor=0.1, size=2.5)
mdb.models['Model-1'].parts['Part-1'].generateMesh()
mdb.models['Model-1'].parts['Part-1'].setElementType(elemTypes=(ElemType(
    elemCode=C3D20R, elemLibrary=STANDARD), ElemType(elemCode=C3D15, 
    elemLibrary=STANDARD), ElemType(elemCode=C3D10H, elemLibrary=STANDARD)), 
    regions=(mdb.models['Model-1'].parts['Part-1'].cells.getSequenceFromMask((
    '[#1 ]', ), ), ))
#Refpoints
mdb.models['Model-1'].parts['Part-1'].ReferencePoint(point=
    mdb.models['Model-1'].parts['Part-1'].InterestingPoint(
    mdb.models['Model-1'].parts['Part-1'].edges[29], MIDDLE))
mdb.models['Model-1'].rootAssembly.regenerate()
mdb.models['Model-1'].parts['Part-1'].Set(name='RP', referencePoints=(
    mdb.models['Model-1'].parts['Part-1'].referencePoints[12], ))
mdb.models['Model-1'].rootAssembly.regenerate()
mdb.models['Model-1'].HistoryOutputRequest(createStepName='press', name=
    'H-Output-2', rebar=EXCLUDE, region=
    mdb.models['Model-1'].rootAssembly.allInstances['Part-1-1'].sets['RP'], 
    sectionPoints=DEFAULT, variables=('U1', 'U2', 'U3', 'UR1', 'UR2', 'UR3'))
mdb.models['Model-1'].rootAssembly.Surface(name='s_Surf-1', side1Faces=
    mdb.models['Model-1'].rootAssembly.instances['Part-1-1'].faces.getSequenceFromMask(
    ('[#200 ]', ), ))
mdb.models['Model-1'].Coupling(controlPoint=
    mdb.models['Model-1'].rootAssembly.instances['Part-1-1'].sets['RP'], 
    couplingType=DISTRIBUTING, influenceRadius=WHOLE_SURFACE, localCsys=None, 
    name='Constraint-1', surface=
    mdb.models['Model-1'].rootAssembly.surfaces['s_Surf-1'], u1=ON, u2=ON, u3=
    ON, ur1=ON, ur2=ON, ur3=ON, weightingMethod=UNIFORM)
mdb.Job(atTime=None, contactPrint=OFF, description='', echoPrint=OFF, 
    explicitPrecision=SINGLE, getMemoryFromAnalysis=True, historyPrint=OFF, 
    memory=90, memoryUnits=PERCENTAGE, model='Model-1', modelPrint=OFF, 
    multiprocessingMode=DEFAULT, name='finalronnagain', nodalOutputPrecision=
    SINGLE, numCpus=3, numDomains=3, numGPUs=0, queue=None, resultsFormat=ODB, 
    scratch='', type=ANALYSIS, userSubroutine='', waitHours=0, waitMinutes=0)
# Save by ronn on 2022_05_02-12.09.16; build 2021 2020_03_06-07.50.37 167380
mdb.saveAs(
pathName=r'C:/temp/finalronnagain')
mdb.jobs['finalronnagain'].submit(consistencyChecking=ON)
  
mdb.jobs['finalronnagain'].waitForCompletion()  

session.Viewport(name='Viewport: 1', origin=(0.0, 0.0), width=94.1484298706055, 
    height=104.883338928223)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports['Viewport: 1'].maximize()
#: The interaction property "IntProp-1" has been created.
#: The interaction "Int-1" has been created.
#: The model database has been saved to "C:\temp\finalronnagain.cae".
#: Job finalronnagain: Analysis Input File Processor completed successfully.
#: Job finalronnagain: Abaqus/Standard completed successfully.
#: Job finalronnagain completed successfully. 
#: Model: C:/temp/finalronnagain.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     1
#: Number of Meshes:             1
#: Number of Element Sets:       3
#: Number of Node Sets:          5
#: Number of Steps:              1
#: The model database has been saved to "C:\temp\finalronnagain.cae".
#odb = session.odbs['C:/temp/finalronnagain.odb']
session.mdbData.summary()
    
o3 = session.openOdb(
name='C:/temp/finalronnagain.odb')
session.viewports['Viewport: 1'].setValues(displayedObject=o3)
odb = session.odbs['C:/temp/finalronnagain.odb']
session.writeFieldReport(fileName='abaqus.rpt', append=ON, 
    sortItem='Node Label', odb=odb, step=0, frame=17, outputPosition=NODAL, 
    variable=(('UR', NODAL, ((COMPONENT, 'UR1'), )), ), stepFrame=SPECIFY)
odb = session.odbs['C:/temp/finalronnagain.odb']
session.writeFieldReport(fileName='abaqus.rpt', append=ON, 
    sortItem='Node Label', odb=odb, step=0, frame=17, outputPosition=NODAL, 
    variable=(('UR', NODAL, ((COMPONENT, 'UR1'), )), ), stepFrame=SPECIFY)

mdb.saveAs(
pathName=r'C:/temp/finalronnagain')


